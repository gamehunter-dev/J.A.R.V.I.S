import requests
import json

def fetch_coding_news():
    url = "https://reddit.com/r/programming/top.json?limit=5"
    headers = {'User-agent': 'JarvisCodingNewsBot 0.1'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            news_items = []
            for post in posts:
                title = post['data']['title']
                url = post['data']['url']
                news_items.append(f"{title}: {url}")
            return "\n".join(news_items)
        else:
            return f"Failed to fetch. Status code: {response.status_code}"
    except Exception as e:
        return str(e)

print(fetch_coding_news())
