# 03 Method: DSSF (Deep State Space Flow)

## 结构图（推荐用作 Figure 1）

```mermaid
flowchart LR
  A[Physics Entities + Knobs (Config)]
  A --> C[Condition Encoder]
  C --> S[Skeleton: Deep SSM/Mamba]
  S --> R[Residual r = x - x_hat]
  C --> F[Flow Head (FM/RF)]
  S --> F
  F --> Xhat[Sample residual r_tilde]
  Xhat --> Sum[x_tilde = x_hat + r_tilde]
  Sum --> Sen[Sensor Corruptor]
  Sen --> Out[Waveform + Meta]
  Out --> Eval[Metrics: ECS/RDS/SAS/PCS/FVD]
```

---

## 模型分解（最小闭环）

### (1) Condition Encoder
输入：bearing geometry + speed_profile + fault_type y + severity s(t) + sensor knobs  
输出：条件向量/序列 c（供 Skeleton 与 Flow 使用）

### (2) Skeleton：Deep SSM（推荐 Mamba）
目标：输出骨架 \hat x，承载“机理结构”（冲击节律/特征频率/趋势）

关键：加入样本级潜变量 z0，避免骨架过于确定：
$$
z_0\sim\mathcal N(0,I)
$$

### (3) Texture：Residual Flow Matching / Rectified Flow
目标：学残差分布 r = x-\hat x  
采样快（10–20 步），适合工业落地

### (4) Sensor Corruptor
目标：把“域差异”变成显式 knobs，而不是交给模型瞎学  
例如 clipping/dropout/quantization/snr

---

## 批判 → 改进 → 再批判（方法层）

### 批判：Skeleton = f(condition) 可能太“死”
**改进**：引入 z0（样本级随机性），把结构随机性留给 Skeleton，纹理随机性交给 Flow。

### 再批判：Flow 可能偷偷学结构，削弱可控性
**改进**：1) 训练时强制 residual 只学习高频/纹理（例如对 residual 先带通）；2) 用可控指标联合筛选不合格样本（Table 1）。
