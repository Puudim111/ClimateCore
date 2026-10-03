import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_climate_videos():
    if not YOUTUBE_API_KEY:
        return []

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": "mudanças climáticas aquecimento global",
        "type": "video",
        "maxResults": 6,
        "order": "relevance",
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Erro na API do YouTube:", response.text)
        return []

    data = response.json()

    videos = []

    for item in data.get("items", []):
        video_id = item.get("id", {}).get("videoId")

        if video_id:
            videos.append({
                "id": video_id,
                "title": item["snippet"]["title"]
            })

    return videos