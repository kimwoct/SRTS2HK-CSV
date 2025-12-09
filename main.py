#!/usr/bin/env python3
"""Convert SRT subtitle files to CSV format with simplified-to-traditional conversion."""

import re
from pathlib import Path
from convert import convert_s2t, INPUT_FOLDER, OUTPUT_FOLDER


def srt_to_csv(srt_text: str) -> str:
    """
    Converts SRT subtitle text to CSV format.

    This function takes SRT (SubRip Text) subtitle content and transforms it into
    a CSV string with columns: Index, Time, Content. Each subtitle block in the
    SRT file becomes a row in the CSV.

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

    # Write CSV file
    output_path.write_text(csv_content, encoding='utf-8')

    print(f"CSV: {input_path} -> {output_path}")
    return output_path


def process_all_files():
    """
    Process all SRT files: convert to traditional Chinese and then to CSV.
    """
    # Ensure input folder exists
    if not INPUT_FOLDER.exists():
        INPUT_FOLDER.mkdir(parents=True, exist_ok=True)
        print(f"Created input folder: {INPUT_FOLDER}")
        print(f"Please place your SRT files in the '{INPUT_FOLDER}' folder and run again.")
        return
    
    # Find all SRT files
    srt_files = list(INPUT_FOLDER.glob("*.srt"))
    
    if not srt_files:
        print(f"No SRT files found in '{INPUT_FOLDER}'")
        return
    
    for srt_file in srt_files:
        # Step 1: Convert simplified to traditional Chinese
        traditional_srt = convert_s2t(srt_file, OUTPUT_FOLDER)
        # Step 2: Convert traditional SRT to CSV
        convert_srt_to_csv(traditional_srt, OUTPUT_FOLDER)
    
    print(f"\nProcessed {len(srt_files)} file(s) -> SRT & CSV pairs in '{OUTPUT_FOLDER}'")


def main():
    process_all_files()


if __name__ == "__main__":
    main()
