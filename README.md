# Politifact Data Scraper

## Overview
This Python script, `scraper.py`, is designed to scrape political fact-checking data from the Politifact website. It iteratively visits pages, extracts quotes and their associated truthfulness labels, and then saves this scraped data into a CSV file.

## Requirements
- Python 3.x
- `beautifulsoup4==4.12.2`
- `Requests==2.31.0`

These dependencies can be installed via `pip install -r requirements.txt`.

## Usage
Run the script using Python:
```bash
python scraper.py
```
This will scrape data from the Politifact website and store it into a CSV file, named `politifact_data.csv`, which can be used for data analysis or machine learning purposes.

## Output
The script outputs a CSV file with two columns:
- `Quote`: Contains the scraped quotes.
- `Label`: Contains the corresponding truthfulness labels.

## Disclaimer
This script is for educational purposes only. Please ensure you comply with Politifact's terms of service when using this script.