import requests

url = "https://phreddy-blog.onrender.com/"
response = requests.get(url)

# Process the response as needed
print(response.text)
