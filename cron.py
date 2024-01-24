import requests

url = "https://phreddy-blog.onrender.com/"
response = requests.get(url)

print(response.text)
