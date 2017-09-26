import tweepy
import secret
import BibleVerses

# Secret is not include but just defines the four properties below. Create your own
cfg = { 
	"consumer_key"        : secret.consumerKey,
	"consumer_secret"     : secret.consumerSecret,
	"access_token"        : secret.accessKey,
	"access_token_secret" : secret.accessSecret 
	}

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)


def tweetMessage(message):
	api = get_api(cfg)
	tweet = message
	status = api.update_status(status=tweet)

def splitTweet(message):
	end = message
	tweets = []
	while len(end) > 0:
		if len(end) > 120:
			first = end[:120]
			first = first[:first.rfind(' ')]
			tweets.append(first)
			end = end[len(first)+1:]
		else:
			tweets.append(end)
			end = ""
	return tweets

def tweetVerse(i):
	location = BibleVerses.convert_absolute(i)
	scripture = BibleVerses.get_verse(location)
	tweets = splitTweet(scripture)
	for tweet in tweets:
		tweetMessage(tweet)


