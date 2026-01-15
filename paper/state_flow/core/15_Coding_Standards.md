# 15 Coding Standards (让 Agent 不踩坑)

## 命名
- 模型：`DSSF`
- 任务：`GEN_DSSF_PhysicsAware`
- 指标：`PCS, ECS, RDS, SAS, FVD`

## 结构
- 每个模块提供 `from_config(cfg)` 或 `build(cfg)`
- 不在训练主循环写特例 if-else，全部通过 registry 映射
- 所有随机数用统一 seed，并写入 meta

## 日志与产物（必须）
- 保存 config snapshot（yaml）
- 保存关键图：real / skeleton / dssf（波形 + 包络谱）
- 保存指标 csv/json
- 保存 meta（knobs + derived frequencies）

## 单元测试（建议最少 3 个）
- BearingKinematics：已知 rpm 输出频率正确
- PCS：对合成正弦/调制信号输出合理
- FVD：同分布应接近 0，数值稳定
