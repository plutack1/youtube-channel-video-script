import os
from dotenv import load_dotenv
import requests

import json
import csv
load_dotenv()
channel_id = os.getenv("channel_id")
api_key = os.getenv("api_key")

print(api_key)
next_page_token = ""
url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key + "&part=contentDetails"
response = requests.get(url)
data = response.json()

upload_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']


with open("videos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Publish Date"])

    while True:
        url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + upload_id + "&key=" + api_key + "&pageToken=" + next_page_token
        response = requests.get(url)
        data = response.json()


        for item in data['items']:
            title = item['snippet']['title']
            published_at = item['snippet']["publishedAt"]
            writer.writerow([title, published_at])

        # if "nextPageToken" in data:
        #     next_page_token = data["nextPageToken"]
        else:
            break