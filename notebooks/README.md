# 📓 Notebooks Directory

This folder contains all the Jupyter notebooks used in the **"Predicting Price Moves with News Sentiment"** project. The notebooks are organized by functionality: EDA, sentiment correlation analysis, and quantitative technical analysis for individual tickers.

## 📁 Contents

### 1. `eda_news.ipynb`
- **Purpose**: Performs exploratory data analysis (EDA) on raw analyst news data.
- **Key Tasks**:
  - Parses and filters news articles by ticker.
  - Analyzes headline lengths, publisher counts, and daily article frequency.
  - Prepares data for sentiment correlation.

---

### 2. Correlation Analysis Notebooks

These notebooks investigate the relationship between news sentiment and stock price movement for individual tickers using Pearson correlation.

- `correlation_analysis_AAPL.ipynb`
- `correlation_analysis_AMZN.ipynb`
- `correlation_analysis_GOOG.ipynb`
- `correlation_analysis_META.ipynb`
- `correlation_analysis_MSFT.ipynb`
- `correlation_analysis_NVDA.ipynb`
- `correlation_analysis_TSLA.ipynb`

**Each notebook includes**:
- Daily sentiment aggregation.
- Price change computation.
- Pearson correlation and p-value calculations.
- Time series plots and statistical interpretation.

---

### 3. Quantitative Analysis Notebooks

These notebooks apply traditional quantitative analysis techniques using technical indicators for the same set of tickers.

- `quantitative_analysis_AAPL.ipynb`
- `quantitative_analysis_AMZN.ipynb`
- `quantitative_analysis_GOOG.ipynb`
- `quantitative_analysis_META.ipynb`
- `quantitative_analysis_MSFT.ipynb`
- `quantitative_analysis_NVDA.ipynb`
- `quantitative_analysis_TSLA.ipynb`

**Indicators included**:
- SMA, EMA, RSI, MACD
- Daily return, volatility
- Visualizations for trend analysis and potential buy/sell signals

---

### 4. `summarize_correlation.ipynb`
- **Purpose**: Consolidates and summarizes correlation results across all tickers.
- **Output**: A comparison table with correlation coefficients and significance levels to support investment insights.

---

### 5. `__init__.py`
- Empty file to mark this directory as a Python module if needed for imports.

---

### 📌 Notes
- All notebooks depend on shared utilities from the `scripts/` directory.
- Ensure the virtual environment is activated (`.venv`) and dependencies installed via `requirements.txt`.

---

### 📂 Parent Project Structure

