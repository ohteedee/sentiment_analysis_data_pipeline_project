import tweepy
import credentials
import pymongo



def get_auth_handler():
    """
    Function for handling Twitter Authentication. See course material for 
    instructions on getting your own Twitter credentials.
    """
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
    return auth


def get_full_text(status):
    """Returns the full text of a (re)tweet"""
    try:
        return status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return status.full_text


if __name__ == '__main__':
    auth = get_auth_handler()
    api = tweepy.API(auth)

    # connect to mongoDB
    client = pymongo.MongoClient(host='mongodb', port=27017)
    db = client.twitter
    collection = db.tweets

    cursor = tweepy.Cursor(api.search,
            q = "tsla",
            lang = "en",
            tweet_mode = "extended").items(100)

    for status in cursor:
        print(f'tweet {status.full_text}')
        collection.insert_one({"text":status.full_text})