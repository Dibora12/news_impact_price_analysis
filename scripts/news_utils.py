import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources if not already available
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# ---------------------- Data Load and Clean ----------------------

def load_news_data(filepath):
    df = pd.read_csv(filepath)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

# ---------------------- Date Processing ----------------------

def parse_dates(df):
    df['date'] = pd.to_datetime(df['date'], utc=True, format="mixed")
    df['date_only'] = df['date'].dt.date
    return df

# ---------------------- Ticker Filtering ----------------------

def filter_by_ticker(df, ticker):
    return df[df['stock'] == ticker]

# ---------------------- Headline Preprocessing ----------------------

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return [t for t in tokens if t.isalpha() and t not in stop_words]

def add_token_column(df):
    df['tokens'] = df['headline'].apply(preprocess_text)
    return df

# ---------------------- Descriptive Stats ----------------------

def compute_headline_length_stats(df):
    df['headline_length'] = df['headline'].apply(len)
    return df['headline_length'].describe()

def publisher_article_counts(df):
    return df['publisher'].value_counts()

# ---------------------- Daily Frequency ----------------------

def daily_article_counts(df):
    return df['date_only'].value_counts().sort_index()

def plot_daily_article_frequency(daily_counts, title='Daily Article Frequency'):
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.tight_layout()
    plt.show()

# ---------------------- Word Frequency ----------------------

def compute_word_frequencies(df, top_n=10):
    all_tokens = [token for tokens in df['tokens'] for token in tokens]
    word_freq = Counter(all_tokens)
    return dict(word_freq.most_common(top_n))

def plot_top_words(word_freq_dict):
    plt.figure(figsize=(10, 5))
    plt.bar(word_freq_dict.keys(), word_freq_dict.values(), color='skyblue')
    plt.title('Top Words in Headlines')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# ---------------------- Utility ----------------------

def extract_publisher_domain(publisher):
    if '@' in publisher:
        return publisher.split('@')[1]
    return publisher

def add_publisher_domain(df):
    df['publisher_domain'] = df['publisher'].apply(extract_publisher_domain)
    return df

def top_publisher_domains(df, top_n=10):
    return df['publisher_domain'].value_counts().head(top_n)
