#!/usr/bin/env python3
"""Convert SRT subtitle files to CSV format."""

import re
from pathlib import Path


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


def convert_srt_to_csv(input_file: str, output_file: str | None = None) -> None:
    """
    Convert an SRT file to CSV format.

    Args:
        input_file: Path to the input SRT file.
        output_file: Path to the output CSV file. If None, creates a new file with .csv extension.
    """
    input_path = Path(input_file)

    if output_file is None:
        output_path = input_path.with_suffix('.csv')
    else:
        output_path = Path(output_file)

    # Read SRT file
    srt_text = input_path.read_text(encoding='utf-8')

    # Convert to CSV
    csv_content = srt_to_csv(srt_text)

    # Write CSV file
    output_path.write_text(csv_content, encoding='utf-8')

    print(f"Converted: {input_path} -> {output_path}")


def main():
    # Convert the traditional Chinese SRT to CSV
    convert_srt_to_csv("1209_traditional.srt")


if __name__ == "__main__":
    main()
