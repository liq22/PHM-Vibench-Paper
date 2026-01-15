# 07 Experiment Plan (MVP → Ablation → Paper Tables)

## 目标：三张主表 + Figure 1

- Figure 1：物理过程 ↔ DSSF 生成过程（含指标对齐）
- Table 1：可证伪（ECS/RDS/SAS）
- Table 2：保真度（PCS/FVD）vs baselines
- Table 3：下游增益（小样本/跨域）

---

## Phase 0：Smoke (1 天)

- Skeleton：简单滤波/去噪（快速占位）
- Flow：MLP + FM loss（直线）
- Metric：PCS（先不做变速）

验收：能生成波形，PCS > random baseline。

---

## Phase 1：MVP (两周)

### Week 1：Skeleton（Mamba）
- 加 z0 latent
- 输出骨架可视化

### Week 2：Texture（RF / FM）
- Euler 10–20 steps 采样
- 输出 FVD 与波形对比

---

## 必做 Ablations（4 个）

1) Skeleton-only vs DSSF（纹理贡献）
2) Flow-only vs DSSF（骨架贡献）
3) 去掉 A knobs（ECS 下降）
4) 去掉 C knobs（跨域增益下降）

---

## Baselines（最少也要有）

- GAN（若已有实现）
- Diffusion（若已有实现）
- Flow-only
- Skeleton+Gaussian residual

---

## 批判 → 改进 → 再批判（实验层）

- 批判：只做 CWRU 可能过于简单  
- 改进：至少做一次跨域（CWRU → THU）  
- 再批判：跨域可能只是数据集差异而非工况差异  
- 改进：用 knobs 明确模拟目标域（speed/SNR/quantization），并记录来源
