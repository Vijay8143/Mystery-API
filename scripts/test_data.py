import requests

url = "https://blackbox-interface.vercel.app/api/data"
inputs = ["hello", "123", "racecar", "OpenAI"]

for val in inputs:
    res = requests.post(url, json={"data": val})
    try:
        print(f"Input: {val} =>", res.json())
    except Exception as e:
        print(f"Input: {val} => Failed to decode JSON. Raw response:\n{res.text}")
