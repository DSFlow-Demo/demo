# StepFlow Demo Page - Complete Guide

> **Latest Update: 2026-01-30**
> Removed Multilingual section, Added CFG Ablation experiment

## 📋 Table of Contents
- [Overview](#-overview)
- [Latest Changes](#-latest-changes)
- [Project Structure](#-project-structure)
- [Audio Files Guide](#-audio-files-guide)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [Customization](#-customization)

---

## 🎯 Overview

This is a professional demo page for the **DSFlow** (StepFlow) paper, showcasing one-step flow matching speech synthesis with dual supervision and step-aware architecture. The demo features:

- ✅ **Modern Design**: Clean, responsive layout with gradient backgrounds
- ✅ **Comprehensive Audio Demos**: 40 audio samples across 5 sections
- ✅ **Scientific Rigor**: Ablation studies and quantitative comparisons
- ✅ **Framework Visualization**: Embedded PDF with download option
- ✅ **Mobile-Friendly**: Fully responsive design

---

## 🆕 Latest Changes

### What's New (2026-01-30)

#### ✅ Removed
- **Multilingual Demos Section** (former Section 3)
  - Deleted 8 audio files: `ref_*.wav`, `stepflow_multi_*.wav`
  - Removed English 🇺🇸, Mandarin 🇨🇳, Japanese 🇯🇵, Korean 🇰🇷 demos

- **Citation Section**
  - Removed BibTeX code block
  - Kept footer with basic information

#### ✅ Added
- **CFG Strength Ablation Section** (new Section 3)
  - Based on paper Table 5 (Section C.2)
  - Shows effect of classifier-free guidance (CFG) strength
  - 5 CFG levels: w=0.00, 0.05, 0.10, 0.20, 0.50
  - 10 new audio files: `cfg_w*.wav`
  - **Key Finding**: Student achieves optimal performance at w=0.05 (much lower than teacher's w=0.7) because distillation internalizes the guidance effect

#### 📊 File Statistics
- **Total audio files**: 40 (previously 48)
- **Deleted**: 8 multilingual files
- **Added**: 10 CFG ablation files
- **HTML size**: 28KB (~648 lines)

---

## 📁 Project Structure

```
demo/
├── index.html                      # Main demo page (28KB)
├── resorces/
│   ├── Framework_final.pdf         # Framework architecture diagram
│   └── review_version.pdf          # Paper PDF
├── audio/                          # 40 audio files (4.9MB)
│   ├── Section 1: Quality Comparison (6 files)
│   ├── Section 2: Model Comparison (8 files)
│   ├── Section 3: CFG Ablation (10 files) ⭐ NEW
│   ├── Section 4: Emotion & Prosody (8 files)
│   └── Section 5: Ablation Study (6 files)
├── assets/
│   └── images/                     # Optional PNG images
├── AUDIO_FILES_UPDATED.md          # Audio files documentation
├── CHANGES_SUMMARY.txt             # Detailed change log
└── README.md                       # This file
```

---

## 🎵 Audio Files Guide

### Current Demo Sections

#### Section 1: Quality Comparison (6 files)
Teacher vs StepFlow vs Naive Baseline

| File | Model | Steps | Purpose |
|------|-------|-------|---------|
| `teacher_en_1.wav` | Teacher | 10 | English baseline |
| `teacher_zh_1.wav` | Teacher | 10 | Mandarin baseline |
| `stepflow_en_1.wav` | StepFlow | 1 | English 1-step |
| `stepflow_zh_1.wav` | StepFlow | 1 | Mandarin 1-step |
| `baseline_en_1.wav` | Naive Endpoint | 1 | English naive |
| `baseline_zh_1.wav` | Naive Endpoint | 1 | Mandarin naive |

#### Section 2: Comparison with Other Models (8 files)
StepFlow vs FastSpeech2, VITS, StyleTTS2

| Model | Long EN | Complex ZH |
|-------|---------|------------|
| StepFlow | `stepflow_long_en.wav` | `stepflow_complex_zh.wav` |
| FastSpeech2 | `fastspeech2_long_en.wav` | `fastspeech2_complex_zh.wav` |
| VITS | `vits_long_en.wav` | `vits_complex_zh.wav` |
| StyleTTS2 | `styletts2_long_en.wav` | `styletts2_complex_zh.wav` |

#### Section 3: CFG Strength Ablation (10 files) ⭐ NEW
Demonstrates effect of classifier-free guidance strength

| CFG (w) | English | Mandarin | MOS-N | SIM-o | Description |
|---------|---------|----------|-------|-------|-------------|
| 0.00 | `cfg_w0.00_en.wav` | `cfg_w0.00_zh.wav` | 4.29 | 65% | No guidance |
| **0.05** | `cfg_w0.05_en.wav` | `cfg_w0.05_zh.wav` | **4.32** | **66%** | **Optimal** ⭐ |
| 0.10 | `cfg_w0.10_en.wav` | `cfg_w0.10_zh.wav` | 4.25 | 64% | Moderate |
| 0.20 | `cfg_w0.20_en.wav` | `cfg_w0.20_zh.wav` | 4.10 | 59% | Strong |
| 0.50 | `cfg_w0.50_en.wav` | `cfg_w0.50_zh.wav` | 3.78 | 55% | Very strong |

**Key Insight**: The inverted CFG curve (optimal at w=0.05 vs teacher's w=0.7) occurs because the student learns from teacher@w=0.7 targets during distillation, effectively internalizing the guidance effect. Stronger inference-time CFG conflicts with this internalized guidance, causing quality degradation.

#### Section 4: Emotion & Prosody Control (8 files)
Expressive synthesis preservation

| Emotion | Teacher | StepFlow |
|---------|---------|----------|
| 😊 Happy | `teacher_happy.wav` | `stepflow_happy.wav` |
| 😢 Sad | `teacher_sad.wav` | `stepflow_sad.wav` |
| 😠 Angry | `teacher_angry.wav` | `stepflow_angry.wav` |
| 🎤 News | `teacher_news.wav` | `stepflow_news.wav` |

#### Section 5: Ablation Study (6 files)
Component analysis

| Configuration | English | Mandarin | Components |
|---------------|---------|----------|------------|
| Baseline | `ablation_baseline_en.wav` | `ablation_baseline_zh.wav` | Endpoint only |
| + Dual Sup. | `ablation_dual_en.wav` | `ablation_dual_zh.wav` | + Velocity |
| + Step-Aware | `ablation_stepaware_en.wav` | `ablation_stepaware_zh.wav` | + Tokens |
| Full Model | `stepflow_full_en.wav` | `stepflow_full_zh.wav` | All components |

### Audio Format Specifications
- **Format**: WAV (PCM)
- **Sample rate**: 16 kHz
- **Channels**: Mono
- **Bit depth**: 16-bit
- **Duration**: 3-10 seconds

---

## 🚀 Quick Start

### 1. Replace Audio Placeholders

**Current status**: 10 CFG audio files are silent placeholders. Replace them with real generated samples:

```python
# Example: Generate CFG ablation samples
for cfg_strength in [0.00, 0.05, 0.10, 0.20, 0.50]:
    for lang, text in [('en', english_text), ('zh', chinese_text)]:
        audio = stepflow_model.generate(
            text=text,
            prompt=prompt_audio,
            cfg_weight=cfg_strength,
            steps=1
        )
        save_audio(f'audio/cfg_w{cfg_strength:.2f}_{lang}.wav', audio)
```

**Suggested test sentences**:
- **English**: "The development of artificial intelligence has revolutionized many aspects of modern technology and communication."
- **Mandarin**: "人工智能的发展彻底改变了现代科技和通信的许多方面。"

### 2. Preview the Demo Page

```bash
# Navigate to demo directory
cd /data/papers/demo

# Start local web server
python3 -m http.server 8000

# Open in browser
# http://localhost:8000/index.html
```

Alternative (direct browser open):
```bash
firefox index.html
# or
google-chrome index.html
```

### 3. Test Checklist

- [ ] All 40 audio files play correctly
- [ ] CFG ablation section displays properly
- [ ] Framework PDF loads in iframe
- [ ] Tables render correctly
- [ ] Responsive design works on mobile
- [ ] No console errors

---

## 🌐 Deployment

### Option 1: GitHub Pages

```bash
# Add files to git
git add index.html audio/ resorces/ assets/

# Commit changes
git commit -m "Add StepFlow demo page with CFG ablation"

# Push to GitHub
git push origin main

# Enable GitHub Pages
# Go to: Settings → Pages → Source: main branch
```

### Option 2: Custom Server

Upload the entire `demo/` directory to your web server. Ensure:
- `.wav` files have correct MIME type: `audio/wav`
- `.pdf` files have correct MIME type: `application/pdf`
- Server supports range requests for audio streaming

---

## 🎨 Customization

### Change Color Scheme

Edit `index.html` around lines 18 and 33:

```css
/* Current: Purple to Indigo */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Alternative: Blue to Teal */
background: linear-gradient(135deg, #2E3192 0%, #1BFFFF 100%);

/* Alternative: Warm Sunset */
background: linear-gradient(135deg, #f83600 0%, #f9d423 100%);
```

### Add New Demo Section

Follow the existing pattern:

```html
<div class="demo-section">
    <h3>6. Your New Section</h3>
    <p style="margin-bottom: 20px;">Description...</p>
    <table>
        <thead>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1</td>
                <td><audio controls><source src="audio/your_file.wav"></audio></td>
            </tr>
        </tbody>
    </table>
</div>
```

### Adjust Mobile Responsiveness

Modify the media query at line 296:

```css
@media (max-width: 768px) {
    /* Your mobile styles */
}
```

---

## 📊 Demo Design Philosophy

The demo page is strategically designed to:

1. **Lead with Impact**: Abstract and architecture overview
2. **Show, Don't Tell**: Extensive audio comparisons
3. **Scientific Rigor**: Quantitative results and ablations
4. **Competitive Positioning**: Direct comparisons with SOTA
5. **Transparency**: CFG ablation shows method limitations and insights

### Section Strategy

| Section | Answers Question |
|---------|------------------|
| 1. Quality Comparison | "Is 1-step really as good as 10-step?" |
| 2. Model Comparison | "How does it compare to existing fast TTS?" |
| 3. CFG Ablation | "How does guidance affect distilled models?" ⭐ NEW |
| 4. Emotion & Prosody | "Can it handle expressive speech?" |
| 5. Ablation Study | "What does each component contribute?" |

---

## 🔬 Technical Details

### CFG Ablation Background

Based on paper Section C.2 (Lines 792-824, Page 15):

**Equation**: `v_cfg = (1-w) * v_uncond + w * v_cond`

**Finding**: Student model achieves best results at w=0.05, much lower than teacher's w=0.7. This occurs because:
1. Student is trained on teacher@w=0.7 targets
2. Distillation internalizes the guidance effect
3. Additional inference-time CFG conflicts with internalized guidance
4. Result: Inverted CFG curve compared to typical diffusion models

### Model Architecture

- **Teacher**: 154M parameters, 10 steps, adaLN-Zero conditioning
- **Student**: 118M parameters (-24%), 1 step, step-aware tokens
- **Training**: Dual supervision (endpoint + velocity matching)
- **Dataset**: Emilia 95K hours (English + Mandarin)

---

## 📝 TODO

### Required
- [ ] Replace 10 CFG placeholder audio files with real samples
- [ ] Use consistent prompt audio across all CFG samples
- [ ] Verify audio quality matches paper results

### Optional
- [ ] Convert Framework PDF to high-res PNG
- [ ] Add audio waveform visualizations
- [ ] Create mobile app version
- [ ] Add interactive CFG slider demo

---

## 📚 Additional Resources

- **Paper PDF**: `resorces/review_version.pdf`
- **Framework Diagram**: `resorces/Framework_final.pdf`
- **Change Log**: `CHANGES_SUMMARY.txt`
- **Audio Guide**: `AUDIO_FILES_UPDATED.md`

---

## 🤝 Support

For questions or issues:
1. Check `AUDIO_FILES_UPDATED.md` for audio file details
2. Review `CHANGES_SUMMARY.txt` for modification history
3. Verify browser console for errors
4. Test in different browsers (Chrome, Firefox, Safari)

---

## ✅ Completion Checklist

- [x] Modern, responsive HTML page
- [x] Framework PDF embedded
- [x] 5 comprehensive demo sections
- [x] CFG ablation experiment added ⭐
- [x] Multilingual section removed
- [x] Citation section removed
- [x] 40 audio file structure created
- [ ] **Replace CFG placeholder audio (10 files)**
- [ ] Test in multiple browsers
- [ ] Deploy online

---

**Last Updated**: 2026-01-30
**Version**: 2.0 (CFG Ablation Update)
**Paper**: DSFlow - Dual Supervision and Step-Aware Architecture for One-Step Flow Matching Speech Synthesis

---

*Happy demoing! 🎉 Your research deserves a beautiful showcase.*
