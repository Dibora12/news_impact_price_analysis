import pytest
import pandas as pd
from scripts import news_utils

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'date': pd.date_range('2023-01-01', periods=5),
        'headline': [
            "Apple stock rises on new iPhone release",
            "Amazon faces regulatory scrutiny in Europe",
            "Google invests in AI research lab",
            "Microsoft announces dividend increase",
            "Tesla misses delivery targets"
        ],
        'publisher': ["Reuters", "Bloomberg", "CNBC", "Reuters", "BBC"]
    })

def test_get_headline_length_stats(sample_df):
    stats = news_utils.get_headline_length_stats(sample_df)
    assert "mean" in stats
    assert isinstance(stats["mean"], float)

def test_get_top_publishers(sample_df):
    top = news_utils.get_top_publishers(sample_df, n=2)
    assert len(top) == 2
    assert "Reuters" in top.index or "Bloomberg" in top.index

def test_get_top_keywords(sample_df):
    keywords = news_utils.get_top_keywords(sample_df, n=5)
    assert isinstance(keywords, list)
    assert len(keywords) <= 5
    assert all(isinstance(word, str) for word in keywords)

def test_plot_news_volume_runs(sample_df):
    # Should not raise an exception
    news_utils.plot_news_volume_over_time(sample_df)

def test_plot_wordcloud_runs(sample_df):
    # Should not raise an exception
    news_utils.plot_wordcloud(sample_df)

def test_decompose_sentiment_time_series_runs():
    df_sentiment = pd.DataFrame({
        'date': pd.date_range(start="2023-01-01", periods=30, freq='D'),
        'sentiment': [0.1 * (i % 5) for i in range(30)]
    })
    result = news_utils.decompose_sentiment_time_series(df_sentiment)
    assert hasattr(result, "trend")
    assert hasattr(result, "seasonal")
    assert hasattr(result, "resid")
