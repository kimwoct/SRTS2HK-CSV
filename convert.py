#!/usr/bin/env python3
"""Convert simplified Chinese SRT subtitle file to traditional Chinese and CSV."""

import re
import zhconv
from pathlib import Path

# Folder configuration
INPUT_FOLDER = Path("input")       # Input folder for original SRT files
OUTPUT_FOLDER = Path("output")   # Output folder for converted files

# Create folders if they don't exist
INPUT_FOLDER.mkdir(parents=True, exist_ok=True)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def convert_s2t(input_file: str | Path, output_folder: Path | None = None) -> Path:
    """
    Convert simplified Chinese text file to traditional Chinese.
    
    Args:
        input_file: Path to the input file (simplified Chinese)
        output_folder: Folder for output files. If None, uses OUTPUT_FOLDER.
    
    Returns:
        Path to the converted file.
    """
    input_path = Path(input_file)
    output_dir = output_folder or OUTPUT_FOLDER
    
    # Ensure output folder exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create output filename with '_traditional' suffix in output folder
    output_path = output_dir / f"{input_path.stem}_zh{input_path.suffix}"
    
    # Read input file
    content = input_path.read_text(encoding="utf-8")
    
    # Convert to traditional Chinese (zh-hant)
    converted = zhconv.convert(content, "zh-hant")
    
    # Write output file
    output_path.write_text(converted, encoding="utf-8")
    
    print(f"Converted: {input_path} -> {output_path}")
    return output_path


def srt_to_csv(srt_text: str) -> str:
    """
    Converts SRT subtitle text to CSV format.

    Args:
        srt_text: The full SRT text content as a string.

    Returns:
        A CSV formatted string with headers and data rows.
    """
    # Split srt blocks by empty lines
    blocks = re.split(r'\n\s*\n', srt_text.strip())

    rows = []
    for block in blocks:
        lines = [line.strip() for line in block.split('\n')]
        if len(lines) >= 3:
            index = lines[0]
            time = lines[1]
            content = ' '.join(lines[2:])
            rows.append([index, time, content])

    # Build CSV content
    csv_lines = ['Index,Time,Content']
    for row in rows:
        # Escape double quotes and wrap each cell in quotes
        escaped_row = [f'"{cell.replace(chr(34), chr(34)+chr(34))}"' for cell in row]
        csv_lines.append(','.join(escaped_row))

    return '\n'.join(csv_lines)


def convert_srt_to_csv(input_file: str | Path, output_folder: Path | None = None) -> Path:
    """
    Convert an SRT file to CSV format.

    Args:
        input_file: Path to the input SRT file.
        output_folder: Folder for output files. If None, uses OUTPUT_FOLDER.
    
    Returns:
        Path to the converted CSV file.
    """
    input_path = Path(input_file)
    output_dir = output_folder or OUTPUT_FOLDER
    
    # Ensure output folder exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / f"{input_path.stem}.csv"

    # Read SRT file
    srt_text = input_path.read_text(encoding='utf-8')

    # Convert to CSV
    csv_content = srt_to_csv(srt_text)

    # Write CSV file with UTF-8 BOM for Windows Excel compatibility
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(csv_content)

    print(f"CSV: {input_path} -> {output_path}")
    return output_path


def process_all_srt_files(input_folder: Path | None = None, output_folder: Path | None = None) -> list[Path]:
    """
    Process all SRT files in the input folder.
    
    Args:
        input_folder: Folder containing SRT files. If None, uses INPUT_FOLDER.
        output_folder: Folder for output files. If None, uses OUTPUT_FOLDER.
    
    Returns:
        List of paths to converted files.
    """
    input_dir = input_folder or INPUT_FOLDER
    output_dir = output_folder or OUTPUT_FOLDER
    
    # Ensure input folder exists
    if not input_dir.exists():
        input_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created input folder: {input_dir}")
        print(f"Please place your SRT files in the '{input_dir}' folder and run again.")
        return []
    
    # Find all SRT files
    srt_files = list(input_dir.glob("*.srt"))
    
    if not srt_files:
        print(f"No SRT files found in '{input_dir}'")
        return []
    
    converted_files = []
    for srt_file in srt_files:
        # Step 1: Convert simplified to traditional Chinese
        output_path = convert_s2t(srt_file, output_dir)
        converted_files.append(output_path)
        # Step 2: Convert traditional SRT to CSV
        convert_srt_to_csv(output_path, output_dir)

    print(f"\nProcessed {len(converted_files)} file(s) -> SRT & CSV pairs in '{output_dir}'")
    return converted_files


if __name__ == "__main__":
    # Process all SRT files in the input folder
    process_all_srt_files()
