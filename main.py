import requests
import json
import csv
with open("secrets.txt") as f:
    config = compile(f.read(), "config.txt", "exec")
    exec(config)

channel_id = channel_id
api_key = api_key
next_page_token = ""
url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key + "&part=contentDetails"
response = requests.get(url)
data = json.loads(response.text)
upload_id = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


with open("videos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Publish Date"])

    while True:
        url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + upload_id + "&key=" + api_key + "&pageToken=" + next_page_token
        response = requests.get(url)
        data = json.loads(response.text)

        for item in data["items"]:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            published_at = item["snippet"]["publishedAt"]
            video_url = "https://www.youtube.com/watch?v=" + item["snippet"]["resourceId"]["videoId"]
            writer.writerow([title, description, published_at, video_url])

        if "nextPageToken" in data:
            next_page_token = data["nextPageToken"]
        else:
            break