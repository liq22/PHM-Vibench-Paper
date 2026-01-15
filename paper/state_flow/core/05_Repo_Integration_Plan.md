# 05 Repo Integration Plan (PHM-Vibench, config-first)

## 总原则：最小侵入 + 可复现 + 可评测

### 最小侵入
只新增文件与注册条目，不修改核心训练环节的主逻辑。

### 可复现
每个实验只依赖一个 YAML（允许 override），并输出：
- config snapshot
- seed
- 生成 meta
- 指标报告与图

### 可评测
所有指标通过统一 evaluation 管线触发，输出标准化 json/csv。

---

## 建议目录

```
src/model_factory/Generative/DSSF.py
src/model_factory/Generative/components/
  ConditionEncoder.py
  FlowHead.py
  SensorCorruptor.py

src/task_factory/task/GEN/DSSF_PhysicsAware.py

src/utils/physics/bearing_kinematics.py
src/utils/evaluation/
  pcs.py ecs.py rds.py sas.py fvd.py

configs/experiments/gen_02_dssf_physics.yaml
```

---

## 一次 PR 的提交顺序（强烈建议照做）

### Commit 1: Config + registry
- 新增 YAML（最小可运行）
- registry 增条目（便于 atlas/inspect）

验收：运行 main 不报错、打印出 config。

### Commit 2: Metric-Only（先能算 PCS）
- 增 bearing_kinematics + PCS
- 用真实数据验证 PCS 合理

验收：PCS 对应故障类型更高，且数值范围稳定。

### Commit 3: Skeleton baseline
- 先用简单滤波/AE 输出 skeleton
- 输出对比图（real vs skeleton）

验收：骨架保留周期冲击结构。

### Commit 4: Residual FM/RF
- 实现 FlowHead + FM loss + ODE 采样
- 生成 waveforms

验收：FVD 明显下降，波形更真实。

### Commit 5: A/B/C falsifiability
- 加 ECS/RDS/SAS
- 输出 Table 1

验收：Set→Measure 误差小于预设阈值。
