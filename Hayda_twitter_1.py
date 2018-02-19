import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('')
acct = input('Enter Twitter Account:')
n = int(input("Enter amount of friends: "))
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': str(n)})
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)


def twitter_info():
    """
    This function return information about users with specified keys to txt file
    :return:
    {
    "users": [
        {
            "id": 22028833,
            "screen_name": "msretail",
            "location": "Redmond, WA",
            "followers_count": 12922,
            "friends_count": 5852,
            "created_at": "Thu Feb 26 16:35:16 +0000 2009",
            "lang": "en"
        }
    }
    """
    with open("myFile.json", "w", encoding="utf-8") as file:
        key = ["id", "screen_name", "location", "followers_count", "friends_count", "created_at", "lang"]
        all_info = {}
        lst = []
        for user in js["users"]:
            info_lst = []
            for element in user:
                if element in key:
                    info_lst.append(user[element])
                    info = dict(zip(key, info_lst))
            lst.append(info)
            all_info["users"] = lst
        return json.dump(all_info, file, indent=4)


print(twitter_info())
