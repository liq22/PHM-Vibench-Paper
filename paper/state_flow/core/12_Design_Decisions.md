# 12 Design Decisions (Critique → Improve → Critique)

## D1：为什么用 “Skeleton + Residual Flow”？

### 批判
- 直接生成 x（Flow-only / Diffusion）会很像，但缺乏可控机理，容易“幻觉”
- 纯 SSM 输出太干净，不像工业信号

### 改进
- 把可控结构交给 Skeleton，把难以建模的非高斯纹理交给 Flow
- 每条样本都能被指标审计（Table 1）

### 再批判
- Flow 可能偷偷学结构（投机）
- Skeleton 可能太弱，导致 residual 过重

### 再改进（工程动作）
- residual 训练前做频段限制（高频/纹理）
- skeleton 加 z0 latent + 更强 backbone（Mamba）

---

## D2：为什么选 Mamba 作为 Deep SSM backbone？

### 批判
- Transformer 对长序列成本高
- RNN 可能难以学长依赖

### 改进
- Mamba 是选择性 SSM，线性时间、擅长长序列建模 citeturn0search0

### 再批判
- Mamba 作为 AE/SSM 的实现复杂度更高
**改进**：MVP 先用简单 AE 占位，跑通后再换 Mamba（不改变接口）。

---

## D3：为什么用 FM/RF（而不是 diffusion）？

- FM：simulation-free、训练更稳定 citeturn0search1
- RF：路径更直、采样更快 citeturn0search2
- 时间序列已有 RF 框架（FlowTS）做背书 citeturn0search3

批判：这些方法多在图像/通用时序  
改进：我们把“物理审计”作为核心差异点（Table 1 + PCS）。
