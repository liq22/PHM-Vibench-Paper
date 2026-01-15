# 00 Overview

## TL;DR

DSSF = **可审计的解耦生成**：

- **Skeleton（骨架）**：Deep SSM（建议 Mamba）生成“机理可解释结构”
- **Texture（纹理）**：Flow Matching / Rectified Flow 生成“工业真实残差”
- **Sensor（传感）**：按概率注入采集伪影（clipping/dropout/量化/漂移）做域随机化

最终每条合成样本都能回答：
> “我为什么长这样？”  
因为 config 里写明了物理实体与 knobs，并且我们能用 ECS/RDS/SAS/PCS/FVD 去验证。

---

## DSSF 解决的三类真实痛点

1. **故障数据稀缺**：生成补齐长尾故障/严重度阶段
2. **Domain Gap**：通过 (B)(C) 层 knobs 直接模拟目标域（转速、共振漂移、传感器伪影）
3. **生成模型幻觉污染**：每条样本都能被审计，不合格就丢弃（falsifiable）

---

## 你在代码里要实现的最小闭环

1) 训练：真实数据 x → skeleton \hat x → residual r = x-\hat x → Flow 学 r  
2) 生成：采样 residual \tilde r + skeleton \hat x → 合成 \tilde x → Sensor corruption  
3) 评测：ECS/RDS/SAS/PCS/FVD  
4) 下游：把 \tilde x 混入训练集，测跨域/小样本增益

---

## 批判 → 改进 → 再批判（这不是口号）

- 批判：只做“像”的生成很容易造假、污染训练
- 改进：把 knobs 定义成物理实体，并要求可反证指标
- 再批判：指标可能被“作弊”（例如 PCS 虚高），所以要加防作弊实现细节（见 [[06_Evaluation_Metrics_Spec]] 与 [[13_Risk_Register]]）
