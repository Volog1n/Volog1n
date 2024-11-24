# Funnel Analysis Project

This project analyzes user behavior by matching visit data with purchase data to create a funnel report.

## Description

The script processes two input files:
- `purchase_log.txt`: Contains user purchase data in JSON format
- `visit_log.csv`: Contains user visit data in CSV format

It creates an output file:
- `funnel.csv`: Contains matched visits with purchase categories

## How it works

1. Reads purchase data from purchase_log.txt into memory
2. Processes visit_log.csv line by line (memory efficient)
3. Matches visits with purchases
4. Creates funnel.csv with matched data

## Usage

```bash
python funnel_analysis.py
```

## Input File Formats

### purchase_log.txt
JSON format per line:
```json
{"user_id": "user123", "category": "Продукты"}
```

### visit_log.csv
CSV format:
```
user_id,source
user123,other
```

## Output File Format

### funnel.csv
CSV format:
```
user_id,source,category
user123,other,Продукты
```
