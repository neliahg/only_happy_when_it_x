import requests

url = "https://jsonplaceholder.typicode.com/users/3/posts"
resp = requests.get(url)
resp.raise_for_status()           # Throw if not 2xx
posts = resp.json()               # list of dicts

first_body = posts[0]["body"]

params = {"lat": 32.1, "lon": 34.8, "appid": "YOUR_KEY"}
resp = requests.get("https://api.openweathermap.org/data/2.5/weather",
                    params=params)

headers = {"Authorization": f"Bearer {API_KEY}"}
resp = requests.post("https://api.openai.com/v1/responses",
                     headers=headers, json={"model": "...", "input": "Hi"})