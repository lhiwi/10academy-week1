import talib
import numpy as np
import pandas as pd
import pandas_ta as ta


def test_talib_indicators():
    """Test TA-Lib indicator calculations"""
    # Create sample price data
    prices = np.array([90.0, 92.5, 91.8, 94.2, 93.5, 95.0, 94.2], dtype=float)
    
    # Test SMA
    sma = talib.SMA(prices, timeperiod=3)
    assert len(sma) == len(prices)
    assert not np.isnan(sma[-1])
    
    # Test RSI
    rsi = talib.RSI(prices, timeperiod=3)
    assert len(rsi) == len(prices)
    assert np.nanmin(rsi) >= 0
    assert np.nanmax(rsi) <= 100
    
    # Test Volatility (STDDEV)
    volatility = talib.STDDEV(prices, timeperiod=3, nbdev=1)
    assert len(volatility) == len(prices)
    assert volatility[-1] > 0