# 13 Risk Register (Failure Modes)

| Risk | Symptom | Detection | Mitigation |
|---|---|---|---|
| PCS 虚高 | 生成样本在目标频带插窄峰 | bandpass 后再算 PCS；加多指标筛选 | 频段限制 residual；联合 ECS/RDS |
| Flow 学结构 | 去掉 skeleton 也能生成类似特征频率 | ablation：Flow-only vs DSSF | residual 预处理；强化 skeleton |
| ECS 不稳定 | 同一 λ 得到波动很大 | 多种阈值/归一化对比 | 自适应阈值；固定带通 |
| 变速失效 | 变速下 PCS 无意义 | 变速专门实验 | order tracking 或动态带宽 |
| FVD 不可信 | embedding 选错导致指标偏差 | 多 encoder 验证 | 用领域 encoder（ISFM） |
| 生成污染训练 | 下游性能提升但错误模式增多 | 误报/混淆矩阵分析 | 只用通过 Table 1 审计的样本 |

---

## 迭代用法（每次实验后更新本表）
1) 新发现失败模式 → 加一行  
2) 给出检测方法 → 写单测/脚本  
3) 给出缓解方案 → 写到 TODO 并实现
