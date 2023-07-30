import requests
import json
import csv
with open("secrets.txt") as f:
    config = compile(f.read(), "config.txt", "exec")
    exec(config)

channel_id = channel_id
api_key = api_key
url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key + "&part=contentDetails"
response = requests.get(url)
data = json.loads(response.text)
upload_id = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + upload_id + "&key=" + api_key
response = requests.get(url)
data = json.loads(response.text)
with open("videos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Publish Date"])

    for item in data["items"]:
        title = item["snippet"]["title"]
        publish_date = item["snippet"]["publishedAt"]
        writer.writerow([title, publish_date])