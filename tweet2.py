# Import the Twython class
from twython import Twython
import json
import pandas as pd

creds = ['nDgalakt5nAglyDfCjz5Xvb8y','DpQlErDlkGrUr3LR37OxAalZM7splX0ig4r1qTCsfFXoCWvlHU']

# Instantiate an object
python_tweets = Twython(creds[0], creds[1])

# Create our query
query = {'q': 'mcdonaldsmalaysia',
        'count': 1000,
        'fromDate': '2018-01-01',
        'toDate': '2019-12-12',
        'account_type':'premium'
}

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

print(df)