import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets with content length strictly greater than 15
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
