import requests

url = "https://blackbox-interface.vercel.app/api/alpha"
inputs = ["abc123", "!@#OpenAI", "xyz"]

for val in inputs:
    res = requests.post(url, json={"data": val})
    print(f"Input: {val} =>", res.json())
