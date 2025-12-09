#!/usr/bin/env python3
"""Convert simplified Chinese SRT subtitle file to traditional Chinese."""

import zhconv
from pathlib import Path


def convert_s2t(input_file: str, output_file: str | None = None) -> None:
    """
    Convert simplified Chinese text file to traditional Chinese.
    
    Args:
        input_file: Path to the input file (simplified Chinese)
        output_file: Path to the output file. If None, creates a new file with '_traditional' suffix
    """
    input_path = Path(input_file)
    
    if output_file is None:
        # Create output filename with '_traditional' suffix
        output_path = input_path.parent / f"{input_path.stem}_traditional{input_path.suffix}"
    else:
        output_path = Path(output_file)
    
    # Read input file
    content = input_path.read_text(encoding="utf-8")
    
    # Convert to traditional Chinese (zh-hant)
    converted = zhconv.convert(content, "zh-hant")
    
    # Write output file
    output_path.write_text(converted, encoding="utf-8")
    
    print(f"Converted: {input_path} -> {output_path}")


if __name__ == "__main__":
    # Convert the SRT file
    convert_s2t("1209.srt")
