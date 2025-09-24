# Superstore Visualization Project — Manish Sharma

This repository contains a complete data visualization project built around a sample Superstore dataset.
Run the analysis script to generate cleaned data and charts, inspect the outputs, and use the included instructions to create a Power BI or Tableau dashboard.

## Structure
{
  "data": [
    "Superstore_sample.csv"
  ],
  "src": [
    "analysis.py"
  ],
  "outputs": [
    "charts"
  ],
  "notebooks": [],
  "Screenshots": []
}

## How to run
1. Create a Python 3.8+ environment and install dependencies:

```
pip install pandas matplotlib pillow
```
2. From the project root run:

```
python src/analysis.py
```
3. Outputs (cleaned CSV + charts) will be in `data/` and `outputs/charts/` respectively.

## Notes
- This project includes a small sample dataset `data/Superstore_sample.csv`. For full analysis replace it with the full `Superstore.csv` and re-run the script.
- Use Power BI or Tableau to design the interactive dashboard using `data/Superstore_cleaned.csv` and the charts in `outputs/charts/`.

---
Author: Manish Sharma
