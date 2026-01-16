# DSSF (Deep State Space Flow) — Physics-Auditable Generative Fault/Anomaly Engine for PHM-Vibench

> 确定性机理骨架（Deep SSM/Mamba） + 统计纹理残差（Flow Matching/Rectified Flow） + 传感层域随机化（Sensor artifacts）

这是一套 **项目核心 Markdown 文档**（给本科生级别 Agent/开发者也能快速上手），用于在 `PHM-Vibench` 的 **config-first** 架构内实现一个“可控 + 高保真 + 可证伪”的故障/异常样本生成系统。

- **输入（Config）**：物理实体（几何、转速曲线、故障类型、严重度演化、采集失真）
- **模型（Model）**：Skeleton（Deep SSM/Mamba） + Texture（Flow Matching/Rectified Flow）
- **输出（Artifacts）**：合成波形 + 元数据（knobs/seed/推导频率）+ 评测指标（ECS/RDS/SAS/PCS/FVD）
- **目标（Paper + Engineering）**：不仅“长得像”，还能“被审计、可反证、可复现”，并能提升下游诊断的跨域与小样本性能。

---

## 1 分钟开始

1. 先读：[[STATUS]]（当前阶段 / 下一步 / 约束）  
2. 然后读：[[00_Overview]]  
3. 再读：[[10_Agent_Onboarding]]（两周任务拆解 + 验收标准）  
4. 开发时只要记住一句话：  
   - Skeleton 负责“因果骨架”，Flow 负责“统计纹理”，Sensor 负责“域随机化”。

---

## 文档地图（按重要度）

- [[00_Overview]]：一句话理解 DSSF
- [[01_Background_and_Significance]]：为什么值得做（论文动机）
- [[02_Challenges_and_Scientific_Questions]]：难点与科学问题（可证伪）
- [[03_Method_DSSF]]：方法与模块划分（含图）
- [[04_Theory_and_Derivations]]：关键公式与推导（Obsidian 可拷贝）
- [[06_Evaluation_Metrics_Spec]]：指标定义（ECS/RDS/SAS/PCS/FVD）
- [[05_Repo_Integration_Plan]]：如何接入 PHM-Vibench（最小改动）
- [[07_Experiment_Plan]]：实验安排（MVP→Ablation→Tables）
- [[08_Table_Templates]]：表格模板（直接填数）
- [[09_TODO_and_Backlog]]：路线图（优先级）
- [[12_Design_Decisions]]：为什么这么设计（批判→改进→再批判）
- [[13_Risk_Register]]：风险登记表（失败模式与应对）
- [[14_Minimal_Config_Examples]]：最小可运行 YAML 示例
- [[15_Coding_Standards]]：代码规范（让 Agent 不踩坑）
- [[STATUS]]：当前状态（每次任务结束必须更新）
- [[ITERATION_LOG]]：迭代日志（追加式）
- [[ITERATION_TEMPLATE]]：每次迭代如何“批判→改进→再批判”

更新时间：2026-01-14
