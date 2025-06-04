# Financial News Sentiment Analysis

![CI Status](https://github.com/lhiwi/Financial-analysis-Week1/workflows/Python%20CI/CD/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue)

> Week 1 challenge solution for 10 Academy AI Mastery program analyzing correlations between financial news sentiment and stock movements.

## Features
- NLP sentiment analysis of financial headlines
- Technical indicators (RSI, MACD) with TA-Lib
- Automated CI/CD pipeline with GitHub Actions
- Comprehensive exploratory data analysis

## Project Structure
├── .github/workflows/ # CI/CD pipelines
├── data/ # Financial datasets
├── notebooks/ # Jupyter notebooks
│ └── eda.ipynb # EDA implementation
├── plots/ # Generated visualizations
├── reports/ # Documentation
├── src/ # Source code
├── tests/ # Test cases
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## Setup & Execution
```bash
# 1. Clone and setup
- git clone https://github.com/lhiwi/Financial-analysis-Week1.git
- cd Financial-analysis-Week1
- python -m venv .venv
- .\.venv\Scripts\activate
- pip install -r requirements.txt

# 2. Run analyses
- jupyter notebook notebooks/eda.ipynb  # Task 1
- python scripts/task2_analysis.py     # Task 2
```

## Task 1: News EDA Results
- Headlines: Avg length 62 chars (range 10-120)
- Top Publishers: SeekingAlpha (12,842), Benzinga (8,927), Bloomberg (7,563)
- Publication Patterns:
                        Peak hours: 9-11 AM EST
                        Peak day: Tuesday (18.7% of weekly volume)
- Top Keywords: Earnings, Stocks, Report, Price, Target

### Task 2: Technical Analysis
Indicators:
        - Moving Averages (SMA20, EMA50)
        - Momentum (RSI14, MACD)
        - Volatility (20-day StDev)
        - Daily returns

Output:
        - Technical charts for each stock
        - Indicator correlation matrices

### Next Steps
- Task 3: News-stock correlation analysis
- Final report preparation
