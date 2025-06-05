# streamlit_app.py: News Sentiment & Stock Correlation Dashboard

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from pathlib import Path

st.title(" News Sentiment vs Stock Movement Dashboard")
st.markdown("""
This dashboard visualizes how daily news sentiment may relate to stock returns, using lagged correlation analysis.
""")

# --- File paths ---
BASE_DIR = Path.cwd().parent
DATA_DIR = BASE_DIR / "data"

# --- Sidebar Config ---
st.sidebar.header("Configuration")

# Ticker selector
sample_ticker = st.sidebar.selectbox("Select Stock Ticker", options=["AAPL"], index=0)

# Load data
@st.cache_data
def load_data():
    news = pickle.load(open(DATA_DIR / "cleaned_analyst_ratings.pkl", "rb"))
    stock = pickle.load(open(DATA_DIR / f"{sample_ticker}_with_indicators.pkl", "rb"))
    return news, stock

news, stock = load_data()

# Sentiment Processing
daily_sentiment = news.groupby('date')['sentiment_polarity'].mean().reset_index()
daily_sentiment['date'] = pd.to_datetime(daily_sentiment['date']).dt.date
daily_sentiment['sentiment_polarity_lag1'] = daily_sentiment['sentiment_polarity'].shift(1)

# Merge Datasets
stock['date'] = pd.to_datetime(stock['date']).dt.date
merged = pd.merge(stock, daily_sentiment[['date', 'sentiment_polarity_lag1']], on='date', how='inner')

# --- Filter Date Range ---
date_min = merged['date'].min()
date_max = merged['date'].max()
date_range = st.sidebar.date_input("Select Date Range", [date_min, date_max], min_value=date_min, max_value=date_max)

# Filter merged data by date
if len(date_range) == 2:
    merged = merged[(merged['date'] >= date_range[0]) & (merged['date'] <= date_range[1])]

# Correlation Heatmap 
st.subheader(" Correlation Heatmap (Lagged Sentiment)")
corr_cols = ['daily_return', 'volatility20', 'rsi14', 'macd', 'sentiment_polarity_lag1']
corr_matrix = merged[corr_cols].dropna().corr()
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax1)
ax1.set_title(f"Correlation Matrix for {sample_ticker}")
st.pyplot(fig1)

# Scatter Plot 
st.subheader("Lagged Sentiment vs Daily Return")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.scatterplot(
    data=merged.dropna(subset=['sentiment_polarity_lag1', 'daily_return']),
    x='sentiment_polarity_lag1',
    y='daily_return',
    ax=ax2
)
ax2.set_title(f"{sample_ticker}: Lagged Sentiment vs Daily Return")
st.pyplot(fig2)

# Raw Data Preview 
st.subheader(" Preview Merged Data")
st.dataframe(merged.head(20))
