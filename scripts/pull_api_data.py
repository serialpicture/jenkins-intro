import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.ok:
    with open("api_data.json", "w") as f:
        json.dump(response.json(), f, indent=2)
    print("API data pulled and saved.")
else:
    print("Failed to fetch API data.")
