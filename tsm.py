import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Step 1: Download stock data
data = yf.download("AAPL", start="2015-01-01", end="2023-01-01")

# Step 2: Preprocess data (use 'Close' price and drop missing values)
data = data[['Close']]
data = data.dropna()

# Ensure the index is a DatetimeIndex
data.index = pd.to_datetime(data.index)

# Step 3: Plot the historical stock prices
data['Close'].plot(title="AAPL Stock Closing Price")
plt.show()

# Step 4: Train-test split
train_size = int(len(data) * 0.8)
train, test = data['Close'][:train_size], data['Close'][train_size:]

# Ensure train and test retain the DatetimeIndex
train.index = pd.to_datetime(train.index)
test.index = pd.to_datetime(test.index)

# Step 5: Fit ARIMA model on training data
model = ARIMA(train, order=(5, 1, 0))  # (p, d, q)
arima_model = model.fit()

# Step 6: Generate predictions for the test set
predictions = arima_model.forecast(steps=len(test))

# Align predictions with the test set index
predictions.index = test.index

# Step 7: Evaluate the model using RMSE
rmse = np.sqrt(mean_squared_error(test, predictions))
print("RMSE on Test Set:", rmse)

# Step 8: Plot historical data, test set, and predictions
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label="Historical Data")
plt.plot(test.index, predictions, label="Forecast", color='red')
plt.legend()
plt.title("AAPL Stock Price Prediction (ARIMA)")
plt.show()
