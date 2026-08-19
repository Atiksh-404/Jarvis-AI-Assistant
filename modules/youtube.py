import os
import requests
import webbrowser
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")


def play_on_youtube(song):

    try:

        url = (
            "https://www.googleapis.com/youtube/v3/search"
            f"?part=snippet"
            f"&maxResults=1"
            f"&q={song}"
            f"&type=video"
            f"&key={API_KEY}"
        )

        response = requests.get(url)
        data = response.json()

        if "items" not in data or len(data["items"]) == 0:
            return None

        video = data["items"][0]

        video_id = video["id"]["videoId"]

        title = video["snippet"]["title"]

        webbrowser.open(
            f"https://www.youtube.com/watch?v={video_id}"
        )

        return title

    except Exception as e:

        print(e)

        return None