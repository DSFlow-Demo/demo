# StepFlow Demo - Audio Files Guide (Updated)

## Overview
This demo page has been updated with the following changes:
- ✅ **Removed**: Multilingual Demos (Section 3) - 8 audio files deleted
- ✅ **Added**: CFG Strength Ablation (New Section 3) - 10 audio files created
- ✅ **Removed**: Citation section
- Total audio files: **41** (previously 49)

## Audio Files by Section

### Section 1: Quality Comparison (6 files)
Teacher vs StepFlow vs Naive Baseline comparison

| File | Purpose |
|------|---------|
| `teacher_en_1.wav` | Teacher model English sample (10 steps) |
| `teacher_zh_1.wav` | Teacher model Mandarin sample (10 steps) |
| `stepflow_en_1.wav` | StepFlow English sample (1 step) |
| `stepflow_zh_1.wav` | StepFlow Mandarin sample (1 step) |
| `baseline_en_1.wav` | Naive endpoint English sample (1 step) |
| `baseline_zh_1.wav` | Naive endpoint Mandarin sample (1 step) |

### Section 2: Comparison with Other Models (6 files)
StepFlow vs FastSpeech2, VITS, StyleTTS2

| File | Purpose |
|------|---------|
| `stepflow_long_en.wav` | StepFlow long English sentence |
| `stepflow_complex_zh.wav` | StepFlow complex Mandarin phonetics |
| `fastspeech2_long_en.wav` | FastSpeech2 long English sentence |
| `fastspeech2_complex_zh.wav` | FastSpeech2 complex Mandarin phonetics |
| `vits_long_en.wav` | VITS long English sentence |
| `vits_complex_zh.wav` | VITS complex Mandarin phonetics |
| `styletts2_long_en.wav` | StyleTTS2 long English sentence |
| `styletts2_complex_zh.wav` | StyleTTS2 complex Mandarin phonetics |

### Section 3: CFG Strength Ablation (10 files) ⭐ NEW
Demonstrates effect of classifier-free guidance strength

| CFG Strength (w) | English File | Mandarin File | MOS-N | SIM-o |
|------------------|--------------|---------------|-------|-------|
| 0.00 (no guidance) | `cfg_w0.00_en.wav` | `cfg_w0.00_zh.wav` | 4.29 | 65% |
| **0.05 (optimal)** | `cfg_w0.05_en.wav` | `cfg_w0.05_zh.wav` | **4.32** | **66%** |
| 0.10 | `cfg_w0.10_en.wav` | `cfg_w0.10_zh.wav` | 4.25 | 64% |
| 0.20 | `cfg_w0.20_en.wav` | `cfg_w0.20_zh.wav` | 4.10 | 59% |
| 0.50 | `cfg_w0.50_en.wav` | `cfg_w0.50_zh.wav` | 3.78 | 55% |

**Key Finding**: The student achieves optimal performance at w=0.05 (much lower than teacher's w=0.7) because distillation internalizes the teacher's guidance effect.

### Section 4: Emotion & Prosody Control (8 files)
Demonstrates expressive control in 1-step synthesis

| Emotion | Teacher File | StepFlow File |
|---------|-------------|---------------|
| 😊 Happy/Excited | `teacher_happy.wav` | `stepflow_happy.wav` |
| 😢 Sad/Calm | `teacher_sad.wav` | `stepflow_sad.wav` |
| 😠 Angry/Intense | `teacher_angry.wav` | `stepflow_angry.wav` |
| 🎤 News/Professional | `teacher_news.wav` | `stepflow_news.wav` |

### Section 5: Ablation Study (6 files)
Component analysis showing contribution of each module

| Configuration | English File | Mandarin File | Components |
|---------------|--------------|---------------|------------|
| Baseline | `ablation_baseline_en.wav` | `ablation_baseline_zh.wav` | Endpoint only |
| + Dual Supervision | `ablation_dual_en.wav` | `ablation_dual_zh.wav` | Endpoint + Velocity |
| + Step-Aware Arch | `ablation_stepaware_en.wav` | `ablation_stepaware_zh.wav` | Step-aware tokens |
| Full StepFlow | `stepflow_full_en.wav` | `stepflow_full_zh.wav` | All components |

## Removed Files (Multilingual Section)
The following files were removed from the demo:
- `ref_en.wav`, `ref_ja.wav`, `ref_ko.wav`, `ref_zh.wav` (reference audio)
- `stepflow_multi_en.wav`, `stepflow_multi_ja.wav`, `stepflow_multi_ko.wav`, `stepflow_multi_zh.wav` (multilingual synthesis)

## File Statistics
- **Total files**: 41 audio files
- **Section 1**: 6 files
- **Section 2**: 8 files
- **Section 3 (NEW)**: 10 files
- **Section 4**: 8 files
- **Section 5**: 6 files
- **Deleted**: 8 multilingual files
- **Added**: 10 CFG ablation files

## Audio Format Requirements
All audio files should be:
- **Format**: WAV (PCM)
- **Sample rate**: 16 kHz
- **Channels**: Mono (1 channel)
- **Bit depth**: 16-bit
- **Duration**: 3-10 seconds (varies by content)

## Generating Real Audio Samples

### For CFG Ablation (Section 3)
To replace the placeholder files with real audio:

```python
# Example: Generate audio with different CFG strengths
for cfg_strength in [0.00, 0.05, 0.10, 0.20, 0.50]:
    audio = stepflow_model.generate(
        text=test_text,
        prompt=prompt_audio,
        cfg_weight=cfg_strength,
        steps=1
    )
    save_audio(f'cfg_w{cfg_strength:.2f}_en.wav', audio, sr=16000)
```

### Suggested Test Sentences
**English**: "The development of artificial intelligence has revolutionized many aspects of modern technology and communication."

**Mandarin**: "人工智能的发展彻底改变了现代科技和通信的许多方面。"

## Testing the Demo Page

```bash
# Start a local web server
cd /data/papers/demo
python3 -m http.server 8000

# Open in browser
# http://localhost:8000/index.html
```

## Notes
1. All current audio files are **silent placeholders** - replace with real generated samples
2. The CFG ablation demonstrates the paper's finding that distilled models internalize guidance
3. Keep audio files consistent in quality and recording conditions for fair comparison
4. Use the same prompt audio across all samples in each section for consistency
