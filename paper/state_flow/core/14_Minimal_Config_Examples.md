# 14 Minimal Config Examples (可直接复制)

## 14.1 最小训练配置（常转速）

```yaml
experiment_name: "gen_min_dssf_cwru"

task:
  name: "GEN_DSSF_PhysicsAware"
  physics_entity:
    bearing_geometry:
      n_ball: 9
      ball_diameter: 7.94e-3
      pitch_diameter: 39.04e-3
      contact_angle_deg: 0.0
  knobs:
    mechanism:
      fault_type: "outer_race"
      impulse_density: {type: "poisson", lambda: 20.0}
      severity_evolution: "linear"
    propagation:
      speed_profile: {type: "constant", rpm: 1797}
      resonance: {base_freq: 3000, drift_factor: 0.0}
    sensor:
      snr_db: 5.0
      artifacts: {clipping_prob: 0.0, dropout_prob: 0.0, quantization_bit: 16}

model:
  name: "DSSF"
  skeleton_backbone:
    name: "Mamba"
    d_model: 128
    n_layer: 4
    use_latent_z0: true
    latent_dim: 32
  flow_head:
    type: "resnet_mlp"
    time_embed_dim: 64

data:
  dataset: "RM_001_CWRU"
  batch_size: 64
  seq_len: 2048

trainer:
  max_epochs: 50

evaluation:
  active: true
  metrics: ["PCS", "FVD"]
  pcs_config:
    harmonics: 3
    bandwidth_tolerance: 0.02
```

## 14.2 变速 + 动态带宽（MVP 变速版）

把 `speed_profile` 换成 ramp，并开启 `bandwidth_tolerance`：
```yaml
propagation:
  speed_profile:
    type: "linear_ramp"
    range_rpm: [1730, 1797]
```

成熟后再加：
```yaml
pcs_config:
  method: "order_tracking"
```
