# 10 Agent Onboarding (本科生可执行版)

## 你要交付的“最终成果”
- 能运行一个 DSSF 实验 YAML
- 生成波形 + 计算 PCS/ECS/RDS/SAS/FVD
- 输出三张表格（见 [[08_Table_Templates]]）
- 代码能被复现（seed + config snapshot）

---

## 30 分钟：先把环境跑起来
- [ ] 能运行 `python main.py --config <any_demo_yaml>`
- [ ] 能找到 configs/ 与 src/ 的结构
- [ ] 打开 [[05_Repo_Integration_Plan]] 看提交顺序

---

## 2 小时：实现 PCS（最有“物理味”）
- [ ] 写 `bearing_kinematics.py`
- [ ] 写 `pcs.py`（bandpass + envelope + spectrum + ratio）
- [ ] 用真实数据算 PCS，确认内圈/外圈可区分

验收：能打印 `PCS(mean±std)`，并保存一张包络谱图。

---

## 2 天：跑通 Skeleton baseline + FM
- [ ] skeleton: 先滤波/AE 占位
- [ ] residual: FM loss + Euler sampling
- [ ] 输出：real / skeleton / dssf 对比波形

验收：肉眼可见纹理更像真实，FVD 降。

---

## 2 周：完成 MVP + 表格
- [ ] Table 2（PCS/FVD）
- [ ] Table 1（ECS/RDS/SAS）
- [ ] Table 3（下游增益）

---

## 你最容易踩的坑（先看）
- PCS 虚高（没 bandpass 或分母没去低频）
- ECS 事件检测不稳（阈值没归一化）
- Flow 学结构（residual 没限制频段）
- 没记录 meta（导致复现失败）
