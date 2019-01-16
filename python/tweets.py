from urllib.request import urlopen
import json

screen_name = "wordpress"

url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + screen_name

with urlopen(url) as response:
    data = json.load(response.read())

    print(len(data), "tweets")

    for tweet in data:
        print(tweet['text'])

# data = json.load(urllib.urlopen(url))
#
# print(len(data), "tweets")
#
# for tweet in data:
#     print(tweet['text'])
