import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

print(data[:2])

parsed = []

for post in data:
    parsed.append({
        "post_id": post["id"],
        "title": post["title"],
        "body": post["body"]
    })

for post in parsed:
    print(json.dumps(post, indent=4))