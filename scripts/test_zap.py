import requests

url = "https://blackbox-interface.vercel.app/api/zap"
inputs = ["zap", "OpenAI", "boom", "ZAPZAP"]

for val in inputs:
    res = requests.post(url, json={"data": val})
    print(f"Input: {val} =>", res.json())
