#!/usr/bin/env python3
"""
Create placeholder audio files for testing the demo page layout.
These are silent WAV files with the correct structure.
Replace them with your actual audio samples when ready.
"""

import os
import wave
import struct

def create_silent_wav(filepath, duration=3.0, sample_rate=22050):
    """Create a silent WAV file"""
    num_samples = int(duration * sample_rate)

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with wave.open(filepath, 'w') as wav_file:
        # Set parameters: 1 channel (mono), 2 bytes per sample (16-bit), sample rate
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        # Write silent audio (all zeros)
        for _ in range(num_samples):
            wav_file.writeframes(struct.pack('<h', 0))

    print(f"Created: {filepath}")

def main():
    base_dir = "audio"

    audio_files = [
        # Section 1: Main Comparison
        "teacher_en_1.wav",
        "teacher_zh_1.wav",
        "stepflow_en_1.wav",
        "stepflow_zh_1.wav",
        "baseline_en_1.wav",
        "baseline_zh_1.wav",

        # Section 2: Model Comparison
        "stepflow_long_en.wav",
        "stepflow_complex_zh.wav",
        "fastspeech2_long_en.wav",
        "fastspeech2_complex_zh.wav",
        "vits_long_en.wav",
        "vits_complex_zh.wav",
        "styletts2_long_en.wav",
        "styletts2_complex_zh.wav",

        # Section 3: Multilingual
        "ref_en.wav",
        "ref_zh.wav",
        "ref_ja.wav",
        "ref_ko.wav",
        "stepflow_multi_en.wav",
        "stepflow_multi_zh.wav",
        "stepflow_multi_ja.wav",
        "stepflow_multi_ko.wav",

        # Section 4: Emotion & Prosody
        "teacher_happy.wav",
        "stepflow_happy.wav",
        "teacher_sad.wav",
        "stepflow_sad.wav",
        "teacher_angry.wav",
        "stepflow_angry.wav",
        "teacher_news.wav",
        "stepflow_news.wav",

        # Section 5: Ablation Study
        "ablation_baseline_en.wav",
        "ablation_baseline_zh.wav",
        "ablation_dual_en.wav",
        "ablation_dual_zh.wav",
        "ablation_stepaware_en.wav",
        "ablation_stepaware_zh.wav",
        "stepflow_full_en.wav",
        "stepflow_full_zh.wav",
    ]

    print("Creating placeholder audio files...")
    print(f"Total files to create: {len(audio_files)}\n")

    for filename in audio_files:
        filepath = os.path.join(base_dir, filename)
        create_silent_wav(filepath, duration=3.0)

    print(f"\n✅ Created {len(audio_files)} placeholder audio files in '{base_dir}/' directory")
    print("\nNext steps:")
    print("1. Replace these silent files with your actual audio samples")
    print("2. Keep the same filenames for the demo page to work correctly")
    print("3. Open index.html in a browser to view the demo")

if __name__ == "__main__":
    main()
