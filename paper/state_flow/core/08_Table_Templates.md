# 08 Table Templates (Copy & Fill)

## Table 1: Falsifiability / Controllability (核心贡献)

| Layer | Knob (Set) | Estimator (Measured) | Score | Pass/Fail Rule |
|---|---:|---:|---:|---|
| A Mechanism | λ = 20/s | \hat{λ} = ____ | ECS = ____ | |\hat{λ}-λ|/λ < 5% |
| B Propagation | drift = 5% | \widehat{drift} = ____ | RDS = ____ | error < 10% |
| C Sensor | p_clip = 0.10 | \hat{p}_clip = ____ | SAS = ____ | |\hat p-p|<0.02 |

---

## Table 2: Fidelity vs SOTA

| Method | PCS ↑ | FVD ↓ | Steps (NFE) ↓ | Notes |
|---|---:|---:|---:|---|
| GAN | | | - | |
| Diffusion | | | 100–1000 | |
| Flow-only | | | 10–20 | |
| Skeleton + Gaussian | | | - | |
| **DSSF (Ours)** | | | 10–20 | |

---

## Table 3: Downstream Utility

### 3.1 Few-shot (1% real)
| Training | Acc/F1 ↑ | AUROC ↑ | Notes |
|---|---:|---:|---|
| 100% real | | | upper bound |
| 1% real | | | baseline |
| 1% real + DSSF | | | target |

### 3.2 Cross-domain
| Train → Test | Baseline | + DSSF (C-layer on) | Gain |
|---|---:|---:|---:|
| CWRU → THU | | | |
| THU → CWRU | | | |
