# StepFlow: Dual Supervision and Step-Aware Architecture for One-Step Flow Matching Speech Synthesis

---

## Abstract
Flow-matching models have enabled high-quality text-to-speech synthesis, but their iterative sampling process incurs substantial computational cost. We introduce **StepFlow**, a modular distillation framework for one-step synthesis. StepFlow addresses two critical limitations in current distillation methods: **process variance** caused by endpoint error accumulation and **structural parameter inefficiency** when reusing continuous-time architectures for discrete tasks. By integrating deterministic velocity alignment with structural adaptation, StepFlow achieves near-teacher quality in a single inference step with significantly reduced parameters.

---

## 🏛️ Methodology: Step-Aware Distillation

<div align="center">
  <img src="Framework.pdf" alt="StepFlow Architecture" style="width:100%; max-width:900px;">
  <p style="text-align: justify; font-size: 0.95em; margin-top: 15px;">
    <strong>Figure 1. Overview of the StepFlow distillation framework.</strong> 
    (Left & Center) The transition from continuous-time <em>adaLN-Zero</em> modulation to our proposed <strong>Step-Aware Architecture</strong>. By replacing heavy MLP-based modulations with lightweight <strong>Step-Aware Tokens</strong>, we align the model capacity with the finite information entropy of discrete few-step tasks. 
    (Right) The <strong>Dual Supervision</strong> strategy. StepFlow synergizes endpoint matching with deterministic <strong>Mean-Velocity Alignment</strong>, reducing training variance by over 60% and ensuring trajectory consistency without extra computational overhead.
  </p>
</div>
---

## 🔊 Audio Demos
All samples are generated in a **Zero-shot** manner using models trained on the **Emilia** dataset.

### 1. One-Step Synthesis Performance
Comparison between the Teacher model (10 steps) and StepFlow (1 step) across diverse linguistic contexts.

| Transcription | Teacher (10 steps) | **StepFlow (1 step)** | Baseline (1 step) |
| :--- | :---: | :---: | :---: |
| "The unique step-aware tokens significantly reduce parameters." | <audio controls><source src="audio/teacher_1.wav"></audio> | <audio controls><source src="audio/stepflow_1.wav"></audio> | <audio controls><source src="audio/base_1.wav"></audio> |
| "Exploring the boundaries of flow-matching distillation." | <audio controls><source src="audio/teacher_2.wav"></audio> | <audio controls><source src="audio/stepflow_2.wav"></audio> | <audio controls><source src="audio/base_2.wav"></audio> |

### 2. Robustness to Reference Prompts (Zero-shot)
StepFlow maintains high speaker similarity even with unseen reference audio.

| Reference Prompt | **StepFlow (1-step Generation)** |
| :--- | :---: |
| <audio controls><source src="audio/ref_1.wav"></audio> | <audio controls><source src="audio/gen_1.wav"></audio> |
| <audio controls><source src="audio/ref_2.wav"></audio> | <audio controls><source src="audio/gen_2.wav"></audio> |

---

## 📈 Key Experimental Results

| Method | NFE | Params | MOS-N ↑ | SIM-O ↑ | RTF ↓ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Teacher (StepTTS) | 10 | 154M | 4.43 ± 0.05 | 0.66 | 0.303 |
| Consistency Dist. | 1 | 154M | 3.82 ± 0.08 | 0.58 | 0.015 |
| **StepFlow (Ours)** | **1** | **118M** | **4.32 ± 0.06** | **0.66** | **0.012** |

> **Note:** StepFlow achieves a **24% reduction in parameters** and a **25x speedup** compared to the teacher model while maintaining comparable prosody and naturalness.
