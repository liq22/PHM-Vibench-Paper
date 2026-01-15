# 09 TODO & Backlog (Prioritized + Acceptance)

## P0：跑通与可复现（必须）
- [ ] 新增 YAML（gen_02_dssf_physics）并能运行
  - Done：main.py 运行成功，打印 config + 保存 snapshot
- [ ] BearingKinematics（几何→频率）
  - Done：给定 rpm 输出 BPFO/BPFI/BSF/FTF，单测通过
- [ ] PCS（bandpass + envelope + dynamic bandwidth）
  - Done：对真实数据内圈/外圈 PCS 可区分
- [ ] Skeleton baseline（滤波/AE 或 Mamba）
  - Done：骨架保留冲击节律（可视化）
- [ ] Residual FM/RF（10–20 steps）
  - Done：生成样本 FVD 下降（比 skeleton-only）

## P1：可证伪三层（论文关键）
- [ ] ECS（事件率一致性）
- [ ] RDS（共振漂移一致性）
- [ ] SAS（伪影概率一致性）
- [ ] FVD（复用 encoder）

## P2：变速与更强控制
- [ ] order-domain PCS（角域重采样）
- [ ] Hawkes 事件过程（自激冲击）
- [ ] guidance：用 PCS/ECS 引导采样（可选）

## P3：工程化
- [ ] on-the-fly 生成混入训练（ratio schedule）
- [ ] 缓存与加速（采样并行）
- [ ] 自动生成论文图与表（reporter）
