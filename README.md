# SRT Converter - 簡體轉繁體字幕轉換工具

Convert simplified Chinese SRT subtitle files to traditional Chinese and export to CSV format using `zhconv`.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Python package manager

## Setup

Install dependencies:
```bash
uv add zhconv
```

## Usage

1. Place your `.srt` files in the `input/` folder
2. Run the conversion script:
   ```bash
   uv run python convert.py
   ```
3. Find the converted files in the `output/` folder:
   - `*_zh.srt` - Traditional Chinese SRT file
   - `*.csv` - CSV file (Excel compatible with UTF-8 BOM)

### Programmatic Usage

```python
from convert import convert_s2t, convert_srt_to_csv, process_all_srt_files

# Convert a single file to traditional Chinese
convert_s2t("input.srt", output_folder=Path("output"))

# Convert SRT to CSV
convert_srt_to_csv("input.srt", output_folder=Path("output"))

# Process all SRT files in input folder
process_all_srt_files()
```

## Supported Conversions

The `zhconv` library supports multiple regional variants:
- `zh-hant` - 繁體 (General Traditional Chinese) ✅ Used
- `zh-tw` - 台灣正體 (Taiwan Traditional)
- `zh-hk` - 香港繁體 (Hong Kong Traditional)
- `zh-hans` - 简体 (Simplified Chinese)
- `zh-cn` - 大陆简体 (Mainland Simplified)

## Project Structure

```
.
├── convert.py          # Main conversion script
├── input/              # Place original SRT files here
├── output/             # Converted files output here
├── pyproject.toml      # Project configuration
└── README.md           # This file
```
