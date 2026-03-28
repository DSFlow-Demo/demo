# English Quality Comparison Audio (10-Step Baseline)

This folder stores the updated English-only demo bundle where the displayed DSFlow rows are backed by a 10-step teacher baseline with CFG = 0.0.

Prompt:
- `librispeech_prompt_short.wav`
- Text: `A cold, lucid indifference reigned in his soul.`

Source metadata:
- `meta.lst`: `/mnt/linbin/lxc/LibriSpeech/LibriSpeech/meta.lst`
- `audio_base_dir`: `/mnt/wby-jfs/audio/test/LibriSpeech`

Rows used in the current web demo:
- `teacher_*`: 10-step teacher
- `baseline_*`: 1-step degraded teacher baseline with CFG = 0.0
- `baseline10_*`: 10-step teacher baseline with CFG = 0.0, used for the displayed DSFlow rows
- `cfg_w*.wav`: 10-step teacher baseline with varying CFG values for the CFG and ablation sections

Cases:
- `main`: `They moved thereafter cautiously about the hut, groping before and about them to find something to show that Warrenton had fulfilled his mission.`
- `ornate` from `1221-135767-0011`: `It was further decorated with strange and seemingly cabalistic figures and diagrams suitable to the quaint taste of the age which had been drawn in the stucco when newly laid on and had now grown hard and durable for the admiration of after times.`
- `engineering` from `2300-131720-0023`: `I think he was perhaps more appreciative than I was of the discipline of the Edison construction department and thought it would be well for us to wait until the morning of the fourth before we started up.`
- `artcritique` from `1188-133604-0002`: `By being studious of color they are studious of division and while the chiaroscurist devotes himself to the representation of degrees of force in one thing unseparated light the colorists have for their function the attainment of beauty by arrangement of the divisions of light.`
