
## 1. Create and activate the virtual environment (only needed once)
python3 -m venv .venv
source .venv/bin/activate

## 2. Install dependencies
pip install -r requirements.txt
#   Or directly: pip install pypdf






# Merge files

## 1. Merge a folder
python src/merge_pdfs.py data/A
python src/merge_pdfs.py data/B
python src/merge_pdfs.py data/C

## 2. To choose a different output location, use -o:
python src/merge_pdfs.py data/A -o output/merged_beginner.pdf
