import tweepy
import time
from datetime import datetime
import openai

# Twitter API keys
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Tweepy setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate tweet content using GPT-3
def generate_tweet_content():
    prompt = "Generate a tweet about the intersection of AI, Cannabis, and Cryptocurrency."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response['choices'][0]['text']

# Function to create a tweet
def create_tweet():
    content = generate_tweet_content()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tweet = f"{content} 🌿🚀 {current_time}"
    hashtags = "#AI #Cannabis #Cryptocurrency"  # Add more hashtags as needed
    tweet += f" {hashtags}"
    return tweet

# Main loop
while True:
    try:
        tweet = create_tweet()
        api.update_status(tweet)
        print(f"Tweeted: {tweet}")
        time.sleep(5400)  # Sleep for 90 minutes (90 * 60 seconds)
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        time.sleep(60)
