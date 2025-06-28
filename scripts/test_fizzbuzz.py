import requests

url = "https://blackbox-interface.vercel.app/api/fizzbuzz"
inputs = ["3", "5", "15", "7", "hello"]

for val in inputs:
    res = requests.post(url, json={"data": val})
    print(f"Input: {val} =>", res.json())
