import requests

url = "https://blackbox-interface.vercel.app/api/time"
res = requests.get(url)
print("Response:", res.json())
