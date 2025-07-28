import requests

# from plotly.graph_objects import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.+json'}
r = requests.get(url, headers=headers)

response_dict = r.json()
repo_dicts = response_dict['items']

# Process the data
stars, labels, repo_links = [], [], []
for repo in repo_dicts:
    # y axis
    stars.append(repo['stargazers_count'])
    # label
    label = f"{repo['owner']['login']}<br />{repo['description']}"
    labels.append(label)
    # repo link (x axis)
    repo_link = f"<a href='{repo['html_url']}'>{repo['name']}</a>"
    repo_links.append(repo_link)

# Make visualization
data = [
    {
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        },
        'opacity': 0.6
    }
]
layout = {
    'title': {
        'text': 'Most-Starred Python Projects on Github',
        'font': {'size': 28}
    },  
    'xaxis': {
        'title': {
            'text' : 'Repositories',
            'font': {'size': 24}
        },
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': {
            'text' : 'Stars',
            'font': {'size': 24}
        },
        'tickfont': {'size': 14}
    }

}

fig={'data': data, 'layout': layout }
offline.plot(fig, filename='python_repos-start-count.html')
