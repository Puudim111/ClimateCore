import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_URL = "https://newsapi.org/v2/everything"


def get_climate_news():
    if not NEWS_API_KEY:
        return []

    params = {
        "q": '"climate change" OR "global warming" OR "CO2" OR "polar ice"',
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 12
    }

    headers = {
        "X-Api-Key": NEWS_API_KEY
    }

    try:
        response = requests.get(
            NEWS_URL,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        articles = []

        for article in data.get("articles", []):
            articles.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "source": article.get("source", {}).get("name"),
                "published_at": article.get("publishedAt"),
                "image": article.get("urlToImage")
            })

        return articles

    except requests.RequestException:
        return []