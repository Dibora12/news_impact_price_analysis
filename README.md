# news_impact_price_analysis

## Project Overview
This project analyzes financial news sentiment to identify correlations with stock market movements for seven stocks: AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA. Using news data from `raw_analyst_ratings.csv` and stock price data from Yahoo Finance, we conduct exploratory data analysis (EDA), quantitative stock analysis, and prepare for sentiment analysis to predict price movements. Developed for the Nova Financial Solutions challenge, this repository emphasizes modularity, reproducibility, and collaboration.

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

## Repository Structure
```
news_impact_price_analysis/
├── .github/
│   └── workflows/
│       └── ci.yml
├── notebooks/
│   ├── eda.ipynb
│   ├── quantitative_analysis_AAPL.ipynb
│   ├── quantitative_analysis_AMZN.ipynb
│   ├── quantitative_analysis_GOOG.ipynb
│   ├── quantitative_analysis_META.ipynb
│   ├── quantitative_analysis_MSFT.ipynb
│   ├── quantitative_analysis_NVDA.ipynb
│   ├── quantitative_analysis_TSLA.ipynb
│   └── README.md
├── scripts/
│   ├── init.py
│   ├── news_utils.py
│   └── README.md
├── src/
│   ├── init.py
├── tests/
│   ├── init.py
├── .gitignore
├── README.md
├── requirements.txt
```


## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/B5W1-News-Sentiment.git
   cd news_impact_price_analysis

   Create Virtual Environment:
   python3 -m venv venv
   source venv/bin/activate  #
   Install Dependencies:

	pip install -r requirements.txt
