# 🛠️ Scripts Directory

This folder contains reusable Python modules that support the data preprocessing, EDA, and analysis workflows for the **"Predicting Price Moves with News Sentiment"** project.

These scripts are imported across multiple notebooks in the `notebooks/` directory to avoid redundancy and promote clean, modular code.

## 📄 Contents

### 1. `news_utils.py`
A utility module for handling news dataset operations and exploratory data analysis.

#### 🔧 Key Functions

- **`load_news_data(path)`**  
  Loads the raw CSV file containing analyst news and returns a DataFrame.

- **`parse_dates(df)`**  
  Ensures proper datetime parsing and handles missing or malformed dates.

- **`filter_by_ticker(df, ticker)`**  
  Filters the news headlines by stock ticker symbol (e.g., AAPL, MSFT).

- **`daily_article_counts(df)`**  
  Computes the number of articles per day for a specific ticker.

- **`plot_daily_article_frequency(df, ticker)`**  
  Generates a time series plot showing how often a ticker appears in headlines.

- **`get_headline_lengths(df)`**  
  Returns descriptive statistics (mean, median, distribution) of headline lengths.

- **`get_top_publishers(df, top_n=10)`**  
  Counts and returns the top publishers by frequency.

- **`tokenize_and_clean(text)`**  
  Tokenizes, lowercases, and removes stopwords from headlines for word frequency analysis.

- **`get_top_words(df, top_n=20)`**  
  Finds the most frequent non-stopword tokens in the news headlines.

---

### 2. `__init__.py`
Marks this folder as a Python package, enabling imports like:
```python
from scripts.news_utils import load_news_data
```


## ⚠️ Notes
Dependencies: Make sure to install required libraries using requirements.txt (e.g., pandas, nltk, matplotlib).

NLTK Setup: Some functions require downloading NLTK stopwords and tokenizers.
```
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
## 📁 Usage Context
These scripts are primarily used in:

eda_news.ipynb — for news data exploration and visualization.

correlation_analysis_*.ipynb — to prepare data for sentiment correlation.

quantitative_analysis_*.ipynb — indirectly when preprocessing ticker-specific news.

