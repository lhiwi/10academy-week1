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
├── .vscode
        ├── settings.json
├── data/
│ ├── cleaned_analyst_ratings.pkl # Processed news sentiment data
│ └── AAPL_with_indicators.pkl # Technical indicators for AAPL
│
├── plots/
│ ├── AAPL_rsi14.png # RSI visualization
│ ├── AAPL_macd.png # MACD components
│ ├── AAPL_returns.png # Daily returns
│ ├── AAPL_volatility.png # 20-day rolling volatility
│ └── AAPL_sentiment_correlation_heatmap.png # Correlation heatmap
│
├── notebooks/ # All development scripts
│ ├── Sentiment_analysis.ipynb # News cleaning & sentiment analysis
│ ├── Technical_analysis.ipynb # Stock indicators using TA-Lib
│ └── Correlation.ipynb # Merge and correlation analysis
│
├── src/
│ └── app.py # Streamlit dashboard
├── tests/ # Test cases
├── .gitignore # Ignore patterns
├── .gitattributes # for large files
├── requirements.txt # Python dependencies
├── README.md

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

## Task 3: News Sentiment–Stock Correlation

**Objective**: Quantify the relationship between news sentiment and daily stock returns.

### Inputs:
- Cleaned news headlines with timestamps
- Stock data with indicators and daily returns

### Processing:
- Sentiment Scoring:
  - Compute polarity using TextBlob on each headline
  - Aggregate daily average sentiment

- Temporal Alignment:
  - Merge sentiment with stock data
  - Apply 1-day lag to sentiment scores

- Correlation Analysis:
  - Calculate Pearson correlation between lagged sentiment and:
    - Daily returns
    - RSI / Volatility / Momentum indicators

### Output:
- Correlation coefficient (sentiment vs return)
- Visualizations:
  - `sentiment_vs_return.png` – Scatter plot of sentiment vs return
  - `correlation_matrix.png` – Heatmap of all metric correlations
  - `sentiment_returns_trend.png` – Sentiment and return time-series plot
- A dashboard using streamlit

### Run:
```bash
python scripts/task3_correlation.py
streamlit run app.py

