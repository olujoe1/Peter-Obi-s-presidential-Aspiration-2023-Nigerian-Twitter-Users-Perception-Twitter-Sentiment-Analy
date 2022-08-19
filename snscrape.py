import snscrape.modules.twitter as sntwitter
import pandas as pd


def get_tweets(max_tweets, key_words):
    maxTweets = max_tweets

    tweets_list = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('since:2022-02-01 until:2022-03-31-filter:links -filter:replies -filter:retweets', key_words).get_items()):
        if i > maxTweets:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.sourceLabel, tweet.username, tweet.retweetCount,
                            tweet.likeCount, tweet.quoteCount,
                            tweet.replyCount, tweet.user.followersCount])

    tweets_df = pd.DataFrame(tweets_list, columns=['date', 'id', 'content', 'Source', 'username',
                                                   'retweetCount', 'likeCount', 'quoteCount',
                                                   'replyCount', 'followersCount'])

    return

tweets_df = get_tweets('peter obi')

