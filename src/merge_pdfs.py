"""Merge all PDF files in a given folder into a single PDF.

Usage:
    python src/merge_pdfs.py data/A
    python src/merge_pdfs.py data/B -o output/intermediate.pdf
"""

import argparse
import re
import sys
from pathlib import Path

from pypdf import PdfWriter


def natural_key(path: Path):
    """Sort naturally by the numbers in the file name, e.g. -1, -3, ..., -99, -101 instead of -1, -101, -103."""
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", path.name)]


def merge_folder(folder: Path, output: Path) -> None:
    pdfs = sorted(
        (p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"),
        key=natural_key,
    )
    if not pdfs:
        sys.exit(f"Error: no PDF files found in {folder}")

    output.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    for i, pdf in enumerate(pdfs, 1):
        print(f"[{i}/{len(pdfs)}] {pdf.name}")
        writer.append(str(pdf))

    with open(output, "wb") as f:
        writer.write(f)
    writer.close()
    print(f"\nDone: merged {len(pdfs)} files, {len(writer.pages)} pages in total -> {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge all PDF files in a folder")
    parser.add_argument("folder", help="Folder containing the PDFs to merge, e.g. data/A")
    parser.add_argument("-o", "--output",
                        help="Output file path, defaults to output/<folder name>.pdf")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        sys.exit(f"Error: folder does not exist: {folder}")

    output = Path(args.output) if args.output else Path("output") / f"{folder.name}.pdf"
    merge_folder(folder, output)


if __name__ == "__main__":
    main()
