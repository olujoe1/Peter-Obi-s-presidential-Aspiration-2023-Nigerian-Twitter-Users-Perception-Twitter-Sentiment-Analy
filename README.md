# Peter-Obi-s-presidential-Aspiration-2023-Nigerian-Twitter-Users-Perception-Twitter-Sentiment-Analy
Twitter Sentiment Analysis
# Introduction
This Data Analytics Project focused on Peter Obi tweets (a presidential aspirant in Nigeria) using Natural Language Processing (NLP) Techniques. Every 4 year in Nigeria there is a change of government or extension of existing one, where every political party present their candidates, Peter Obi as one of the candidates who seem to be widely talked about on twitter after he declared his ambition on one of the political parties.

Sncrape was used to mine tweets about Peter Obi from March 2022 shortly before he declared his ambition till August 2022, the total tweets mined was 387,109k. we made use of several Python libraries like Pandas (for Data Manipulation/Cleaning), Sncrape (for Tweets Mining), NLTK (Natural Language Toolkit library to handle text data), TextBlob (for Sentiment Analysis), Matplotlib, Plotly & WordCloud (for Data Visualization), Emot & emoticon (for Emojis identification/for expressed emotion emoji).

# Content
1. Introduction

2. Data Mining and Concatenation

3. Data Cleaning

5. Handling of Text Column

6. Data Exploratory Analysis

7. Sentiment Analysis

# Data Mining and Concatenation
Sncrape as a mining tool is as easy as biting a pie, after trying a couple of tools including tweepy which requires rigorous process for getting a substantial amount of data from twitter. Snscrape is a scraper for social networking services (SNS), including Facebook, Instagram etc. With it we were able to mine tweets containing ‘Peter Obi’ as our key word, and not #tags because the focus is to know what individual is saying about him, while #tag mostly is used by people to be on the trend table for personal promotion of their tweets, data for six months was scrapped, i.e., from March 4th 2022 till August 4th 2022, the data contains datetime, username, follower counts, like counts, and more other variables.


# mining and concat: (https://user-images.githubusercontent.com/76227858/185472484-489eb233-65f7-4591-b7a6-5a8fc360655d.png)

# Data Cleaning
Through data cleaning process we were able to check for nan and none values in the data frame with pandas, through sncrape we were able to filter for the exact data we wanted, this reduced our work on data cleaning, as the data is free of missing values and duplicates, you can read on sncrape here. However, we modify the data to ensure it is free of irrelevances (emojis) and incorrect information (misspelt word). Date time was created for an insight into the daily data trend in our data.

# Handling text data
Text data i.e., individual tweet contains characters (emojis, punctuation, numbers, rare words, #tags, unfamiliar words, links, @, and stopwords) that can serve as noise in our data, which make it important for our data to be cleaned and properly treated. Some of the above libraries like NLTK helped us to manipulate our string data by changing the texts data into lower case, remove stopwaords, create additional columns, among which a column was created for other aspirants whose names were tweeted alongside peter obi for insight, remove emojis and lemmatize our data.

Also, a column was created for the most ratioed tweets/username, i.e., the tweet with the most negative reactions from other users based on what they tweet about Peter Obi. Social medial as greatly enhanced the use of emojis, as they are used to express emotions, with emoticon, were we able to analysis individual expressions through emojis.

With lemmatizer we were able to get the contextual meaning of every word, unlike stemming that can only get the root of a word maybe with meaning or not, you can read up on that here, after this we created a column for our cleaned text data for sentiment analysis.

# Data exploratory analysis
  
  Charting and Visualization

In this section plotly was chosen as the visualization tool because of it flexibly and reactive screen just like PowerBi in jupyter notebook, we got insights from the variables and a wordcloud was generated with the twitter bird to display the most frequent words.

# Conclusion
This research helped to reveal the intention behind every tweets of individual who tweeted about Peter Obi within the time the data was collected, also tweets have been made consistently after when he revealed his desire to run for the presidency, there were 378.48k distinct tweets, 44% of the tweets has positive connotations, 41% were neutral and 14% were negative, this implies that the majority of the 100.44k distinct induvial talking about him were very much interested in his presidential ambition.

However, there were tweets with neutrality whilst most of it does not indicate indifference, rather the choices of words captured as such does not fall between what TextBlob classified has positive or negative, with the seamless traction there were still tweets with negative connotations, users who are not supporting his presidential ambition.


