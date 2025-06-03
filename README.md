# 📈 Predicting Price Moves with News Sentiment

This project explores the correlation between financial news sentiment and stock price movements for major tech companies. The objective is to assess whether news headlines can serve as predictive indicators for short-term stock returns by combining Natural Language Processing (NLP) and quantitative technical analysis.

## 🧠 Business Objective

Nova Financial Solutions seeks to enhance its financial forecasting capabilities by incorporating news sentiment analysis. The primary goals are:

- **Sentiment Analysis**: Quantify the sentiment of financial news headlines related to publicly traded companies.
- **Correlation Analysis**: Investigate the relationship between daily news sentiment and stock price movements.
- **Investment Insights**: Derive actionable insights that leverage sentiment for potential trading strategies.

---

## 📁 Project Structure
```
├── data/
│ ├── raw_analyst_ratings.csv
│ └── yfinance_data/
│ └── {ticker}historical_data.csv
├── notebooks/
│ ├── eda_news.ipynb
│ ├── quantitative_analysis{ticker}.ipynb
│ ├── sentiment_correlation_{ticker}.ipynb
├── scripts/
│ ├── news_utils.py
│ ├── news_preprocessing.py
├── README.md
└── requirements.txt
```


---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/news-sentiment-stock-correlation.git
   cd news-sentiment-stock-correlation
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

## Datasets
- **News Data**: `../data/raw_analyst_ratings.csv`
  - **Rows**: 1,407,328
  - **Columns**: `headline`, `url`, `publisher`, `date`, `stock`
  - **Date Range**: Starts from June 5, 2020
  - **Notes**:
    - No missing values.
    - `date` converted to UTC.
    - Many entries lack timestamps, necessitating daily-level analysis.
- **Stock Data**: `../data/yfinance_data/{ticker}_historical_data.csv`
  - **Tickers**: AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA
  - **Columns**: `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`, `Dividends`, `Stock Splits`
  - **Date Range**: January 22, 1999 to July 30, 2024 (filtered to June 5, 2020 onward to align with news data)


📊 Key Tasks
## 1: Exploratory Data Analysis (EDA)
Cleaned and parsed news dates.

Analyzed headline lengths, publisher distributions, and time series patterns.

Identified keyword frequencies and topic trends.

## 2: Quantitative Analysis
Loaded historical stock data (Open, High, Low, Close, Volume).

Calculated technical indicators using TA-Lib:

Simple Moving Average (SMA)

Exponential Moving Average (EMA)

RSI (Relative Strength Index)

MACD (Moving Average Convergence Divergence)

Visualized price trends and volatility.

## 3: Sentiment & Correlation Analysis
Applied sentiment analysis using TextBlob on headlines.

Computed daily mean sentiment scores.

Calculated daily returns from stock prices.

Performed Pearson correlation between sentiment and returns.

Applied time series decomposition to observe trend/seasonality in sentiment and returns.


📈 Summary of Results
## 📊 Correlation Results

| Ticker | Correlation | p-value  | N Days | Mean Sentiment | Std Return |
|--------|------------:|---------:|-------:|---------------:|-----------:|
| **META** | **0.2949** | 0.0113   | 73     | 0.0403        | 3.91%      |
| NVDA   | 0.1042     | 0.0005   | 1,124  | 0.0731        | 3.27%      |
| TSLA   | 0.0825     | 0.2135   | 229    | 0.0553        | 5.01%      |
| AAPL   | 0.1079     | 0.4120   | 60     | 0.0448        | 3.96%      |
| GOOG   | 0.0567     | 0.2898   | 351    | 0.0419        | 2.15%      |
| AMZN   | -0.0022    | 0.9912   | 27     | 0.0233        | 2.20%      |
| MSFT   | -0.1827    | 0.5908   | 11     | 0.1554        | 1.06%      |

META showed the strongest statistically significant correlation between news sentiment and returns.

Most other tickers showed weak or insignificant correlation.

## 💡 Investment Insights
Positive Sentiment = Positive Returns: Tickers like META and NVDA with consistently positive sentiment exhibited higher correlation with returns.

Data Volume Matters: Stronger correlations were observed in tickers with larger news sample sizes.

Market Sensitivity: Stocks with higher volatility (e.g., TSLA) did not necessarily show stronger correlation, suggesting market movements aren't always sentiment-driven.

Strategy Suggestion: Consider using sentiment scores as part of a multi-factor model for short-term trading in tickers with high correlation (like META).


## 🔧 Tools & Libraries
pandas, numpy

matplotlib, seaborn

textblob for sentiment analysis

TA-Lib, PyNance for financial indicators

scipy.stats for correlation

statsmodels for time series decomposition

## 🧪 How to Reproduce
Place your news data in data/raw_analyst_ratings.csv.

Download historical stock data into data/yfinance_data/{ticker}_historical_data.csv.

Run the notebooks in sequence:

eda_news.ipynb

quantitative_analysis_{ticker}.ipynb

sentiment_correlation_{ticker}.ipynb

```
🔗 References
TextBlob Documentation

TA-Lib

Statsmodels Seasonal Decomposition
```
