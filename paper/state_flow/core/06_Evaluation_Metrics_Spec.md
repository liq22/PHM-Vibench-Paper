# 06 Evaluation Metrics Spec (ECS / RDS / SAS / PCS / FVD)

## 统一接口建议（工程一致性）

每个 metric 实现：

- `__init__(cfg)`
- `update(batch_fake, meta)` 或 `update(batch_real, batch_fake, meta)`
- `compute() -> dict`
- `reset()`

并保证输出键名稳定（便于自动生成表格）。

---

## 6.1 ECS（Event Consistency Score）— A 机理层

设定冲击率 λ（Poisson/Hawkes），检测事件数 N，窗口 T：
$$
\hat\lambda=\frac{N}{T}
$$
$$
\mathrm{ECS}=1-\frac{|\hat\lambda-\lambda|}{\lambda+\varepsilon}
$$

### 实现细节（防作弊）
- 先带通（围绕共振频带）再包络，减少低频污染
- 阈值与最小间隔（避免把噪声峰当冲击）

---

## 6.2 RDS（Resonance Drift Score）— B 传播层

设定共振漂移 Δf（Hz 或比例），从时频谱估计 \widehat{Δf}：
$$
\mathrm{RDS}=1-\frac{|\widehat{\Delta f}-\Delta f|}{|\Delta f|+\varepsilon}
$$

### 实现建议
- STFT → 每帧取峰值频率 → 回归漂移曲线
- 或对能量带中心频率做跟踪（更稳）

---

## 6.3 SAS（Sensor Artifact Score）— C 传感层

设定伪影概率 p，检测得到 \hat p：
$$
\mathrm{SAS}=1-\frac{|\hat p-p|}{p+\varepsilon}
$$

### 建议检测器
- clipping：出现长段恒定最大/最小值，或梯度为 0 的平台
- dropout：连续 0/NaN/重复值片段
- quantization：值域 level 数显著减少（或最小步长变大）

---

## 6.4 PCS（Physics Consistency Score）— 物理一致性

包络谱能量占比：
$$
\mathrm{PCS}=
\frac{\sum_{k=1}^{K}\int_{kf_0(1-\delta)}^{kf_0(1+\delta)} |E(f)|^2\,df}
{\int_{f>f_{\min}} |E(f)|^2\,df}
$$

### 关键：f0 来自几何推导
- config 存几何 + rpm/rpm_curve
- 在线算 BPFO/BPFI/BSF/FTF

### 防作弊
- 先 bandpass 再 envelope
- 分母剔除极低频（如 f<5Hz）

---

## 6.5 FVD（Fréchet Vibration Distance）— 深特征距离

embedding 由 vibration encoder 提取（建议复用 ISFM backbone pooled feature）。

$$
\mathrm{FVD}=\|\mu_r-\mu_g\|_2^2+
\mathrm{Tr}(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2})
$$

数值稳定：sqrtm 可能产生小虚部，取 real 并做 eps 修正。
