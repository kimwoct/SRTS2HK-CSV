# SRT Converter - 簡體轉繁體字幕轉換工具

Convert simplified Chinese subtitle files to traditional Chinese using `zhconv`.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Python package manager

## Setup

1. Initialize the project (already done):
   ```bash
   uv init --name srt-converter
   ```

2. Install dependencies:
   ```bash
   uv add zhconv
   ```

## Usage

### Convert a subtitle file

Run the conversion script:
```bash
uv run python convert.py
```

This will convert `1209.srt` to `1209_traditional.srt`.

### Convert a different file

Edit `convert.py` and change the filename in the `__main__` block:
```python
if __name__ == "__main__":
    convert_s2t("your_file.srt")
```

Or import the function in Python:
```python
from convert import convert_s2t

convert_s2t("input.srt", "output.srt")
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
├── 1209.srt            # Original subtitle (simplified)
├── 1209_traditional.srt # Converted subtitle (traditional)
├── pyproject.toml      # Project configuration
└── README.md           # This file
```
