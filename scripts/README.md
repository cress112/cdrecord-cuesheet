# Helper Scripts
- convert audio files to PCM quality and normalize loudness in one-liner
```sh
scripts/convert_to_wav.sh files wavs && uv run --env-file .env python -m scripts.loudness_normalizer wavs normalized && rm -rf wavs
```
### convert files to WAV
- place audio files into a directory
- exec
```sh
scripts/convert_to_wav.sh <input_dir_contains_audio_files> <output_dir>
scripts/convert_to_wav.sh files wavs
```
### normalize loudness
- place audio files(.wav) into a directory
- exec
```sh
uv run --env-file .env python -m scripts.loudness_normalizer <input_dir_contains_audio_files> <output_dir>
uv run --env-file .env python -m scripts.loudness_normalizer wavs normalized
```

### shift pitch
- exec
```sh
uv run --env-file .env python -m scripts.pitch_shifter <target_wav_file> <shift_width: +/-(int)>
```

### show total duration
- exec
```sh
scripts/show_total_duration.sh <dir_contains_wav_files>
scripts/show_total_duration.sh ./files
```