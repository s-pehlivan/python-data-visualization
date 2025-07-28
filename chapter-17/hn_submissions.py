from operator import itemgetter
from plotly import offline

import requests

baseurl = 'https://hacker-news.firebaseio.com/v0'
url = f"{baseurl}/topstories.json"
r = requests.get(url)

submission_ids = r.json()
submission_dicts = []

titles, comments = [], []


for id in submission_ids[:30]: 

    try:
        url = f"{baseurl}/item/{id}.json"
        r = requests.get(url)
        response_dict = r.json()
    except:
        print("error in the request")

    url = f"http://news.ycombinator.com/item?id={id}"
    
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': url,
        'comments': response_dict["descendants"]
    }

    submission_dicts.append(submission_dict)

    titles.append(f"<a href='{url}'>{response_dict['title'][:20]}...</a>")
    comments.append(response_dict["descendants"])


data = {
    'type': "bar",
    'x': titles,
    'y': comments
}

layout = {
    'title': {
        'text': 'Most Active Hacker News Stories'
    }
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='hn-posts.html')
