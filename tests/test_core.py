# tests/test_core.py
import talib
from textblob import TextBlob
import numpy as np
import pandas as pd  # Add this


def test_talib_version():
    assert talib.__version__ == "0.6.3"

def test_rsi_calculation():
    prices = np.array([90.0, 92.5, 91.8, 94.2, 93.5], dtype=float)
    rsi = talib.RSI(prices, timeperiod=3)
    assert len(rsi) == len(prices)
    assert not np.isnan(rsi[-1])
    
def test_sentiment():
    blob = TextBlob("Excellent quarterly results")
    assert blob.sentiment.polarity > 0.3