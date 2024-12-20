# Stock Price Prediction Using ARIMA

This project demonstrates how to predict stock prices using historical data and the **ARIMA (AutoRegressive Integrated Moving Average)** model. The dataset consists of daily stock prices for Apple Inc. (`AAPL`) sourced from **Yahoo Finance**. The project focuses on time series modeling, prediction, and evaluation using Root Mean Squared Error (RMSE).

---

## 📖 Project Overview

### **Objective**
- Predict Apple Inc.'s future stock prices using the ARIMA model.
- Evaluate model accuracy using RMSE and visualize predictions against actual data.

### **Key Features**
- **Data Source**: Historical stock data fetched directly from Yahoo Finance.
- **Preprocessing**: Focus on closing prices, handle missing values, and prepare the data for time series analysis.
- **Modeling**: Fit the ARIMA model to training data and forecast future prices.
- **Evaluation**: Assess model performance with RMSE.
- **Visualization**: Compare historical prices with model predictions using matplotlib.

---

## 🛠️ Technologies Used

- **Python**: Programming language for the implementation.
- **Libraries**:
  - `yfinance`: Fetch historical stock data.
  - `pandas`: Data manipulation and preprocessing.
  - `matplotlib`: Data visualization.
  - `statsmodels`: ARIMA modeling.
  - `scikit-learn`: RMSE evaluation.

---

## 📊 Dataset

### **Source**
- Data is fetched directly from [Yahoo Finance](https://finance.yahoo.com/) using the `yfinance` library.
- Stock: **Apple Inc. (AAPL)**.
- Date Range: **January 1, 2015 - January 1, 2023**.

### **Data Description**
- Columns include:
  - **Open**: Price at the beginning of the trading day.
  - **High**: Highest price during the day.
  - **Low**: Lowest price during the day.
  - **Close**: Final price at the end of the trading day (used in this project).
  - **Volume**: Number of shares traded.

---

## 📂 Project Structure

```plaintext
stock-price-prediction/
├── tsm.py              # Main Python script for the project
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .gitignore          # Files to ignore in version control
