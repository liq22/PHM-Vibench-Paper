# 04 Theory & Derivations (可直接拷贝到 Obsidian)

## 4.1 Bearing kinematics：特征频率由几何 + 转速推导

设：
- n：滚动体个数
- d：滚动体直径
- D：节圆直径
- α：接触角
- 转速 rpm → 转频：$$f_r = \frac{\mathrm{rpm}}{60}$$

外圈特征频率：
$$
\mathrm{BPFO}=\frac{n}{2}\left(1-\frac{d}{D}\cos\alpha\right) f_r
$$

内圈特征频率：
$$
\mathrm{BPFI}=\frac{n}{2}\left(1+\frac{d}{D}\cos\alpha\right) f_r
$$

滚动体：
$$
\mathrm{BSF}=\frac{D}{2d}\left(1-\left(\frac{d}{D}\cos\alpha\right)^2\right) f_r
$$

保持架：
$$
\mathrm{FTF}=\frac{1}{2}\left(1-\frac{d}{D}\cos\alpha\right) f_r
$$

---

## 4.2 Flow Matching（FM）：训练向量场（simulation-free）

真实残差：$$r = x-\hat x$$

采样：
$$t\sim U(0,1),\ \epsilon\sim\mathcal N(0,I)$$

直线路径：
$$
r_t = (1-t)\epsilon + t r
$$

目标向量场：
$$
v^\*(r_t,t)=\frac{dr_t}{dt}=r-\epsilon
$$

训练损失：
$$
\mathcal L_{FM}=\mathbb E\big[\|v_\psi(r_t,t,c)-(r-\epsilon)\|_2^2\big]
$$

---

## 4.3 Rectified Flow（RF）：少步数采样

采样 ODE：
$$
\frac{dr_t}{dt}=v_\psi(r_t,t,c),\quad r_0=\epsilon,\quad \tilde r=r_1
$$

工程实现：Euler / RK，10–20 steps 常足够。  
参考：Flow Matching 与 Rectified Flow 的原始论文与时间序列版本（FlowTS）。 citeturn0search1turn0search2turn0search3

---

## 4.4 变速工况：两种可行处理（从易到难）

### 方案 A：动态容差带宽（MVP 先用）
令中心频率 f0 取平均 rpm 推导；带宽按转速波动比例设定：
$$
\Delta f_k = \delta\,k f_0
$$

### 方案 B：Order tracking（成熟版）
把时间域重采样到角域（order domain），让特征峰位置稳定（更严谨）。

---

## 批判 → 改进 → 再批判

- 批判：只用 Hz 域 PCS 在变速下会失真  
- 改进：先用动态带宽，后上 order tracking  
- 再批判：order tracking 需要 rpm_curve/tacho，真实数据未必有  
- 改进：把 rpm_curve 作为可选输入：无则常转速近似，有则启用角域方案
