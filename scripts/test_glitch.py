import requests

url = "https://blackbox-interface.vercel.app/api/glitch"
inputs = ["glitch", "OpenAI", "123", "abcdef"]

for val in inputs:
    res = requests.post(url, json={"data": val})
    print(f"Input: {val} =>", res.json())
