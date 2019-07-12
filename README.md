# Sentiment Analysis Using Real-time Tweets
This program is written using python 3.6.8

The project contribute two functionalities as listed below:
* **Main.py** - You can input any sentence, then program will use TextBlob to analysis your sentence, and then it returns result that is how many percent of positive, negative or neutral.
* **twitter.py** - This script can tell you the sentiments of people regarding to any events happening in the world by analyzing tweets related to that event. It will search for tweets about any topic and analyze each tweet to see how positive or negative it's emotion is. 

## What is Sentiment Analysis?
Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker. A common use case for this technology is to discover how people feel about a particular topic.

## Requirements
* textblob
* tkinter (Python GUI)
* tweepy (For twitter.py)
* Good internet connection (For twitter.py)

### Additional requirements for twitter.py
First of all login from your Twitter account and goto Twitter Apps. Create a new app and goto Keys and access tokens and copy `Consumer Key`, `Consumer Secret`, `Access Token` and `Access Token Secret`. We will need them later.

## Run on your local machine
* Navigate to the directory containing the files and run
> cd path/to/project/Sentiment_Analysis
* Run Main.py *(To analyse your input text)*
> python Main.py
* Run twitter.py *(To scrap tweets about entered topic and analyse them)*
> python twitter.py

### Output
* Main.py - You will be propted to enter your sentence. Type your sentence and hit enter, you will see the sentiment polarity of your sentence.
* twitter.py - You will be prompted to enter the keyword/hashtag you want to analyze and the number of tweets you want to analyze(*Optional* Default value is 5). After typing keyword, hit enter and you will see the overall sentiment polarity of tweets and polarity of individual tweets too.
