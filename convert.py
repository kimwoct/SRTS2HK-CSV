#!/usr/bin/env python3
"""Convert simplified Chinese SRT subtitle file to traditional Chinese."""

import zhconv
from pathlib import Path

# Folder configuration
INPUT_FOLDER = Path("input")       # Input folder for original SRT files
OUTPUT_FOLDER = Path("output")   # Output folder for converted files


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
    output_path = output_dir / f"{input_path.stem}_traditional{input_path.suffix}"
    
    # Read input file
    content = input_path.read_text(encoding="utf-8")
    
    # Convert to traditional Chinese (zh-hant)
    converted = zhconv.convert(content, "zh-hant")
    
    # Write output file
    output_path.write_text(converted, encoding="utf-8")
    
    print(f"Converted: {input_path} -> {output_path}")
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
        output_path = convert_s2t(srt_file, output_dir)
        converted_files.append(output_path)
    
    print(f"\nProcessed {len(converted_files)} file(s)")
    return converted_files


if __name__ == "__main__":
    # Process all SRT files in the input folder
    process_all_srt_files()
