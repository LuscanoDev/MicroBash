import requests

url = param
try:
    networkResponse = requests.get(url)
    print(networkResponse.text)
except requests.exceptions.RequestException as e:
    print(f"Error accessing the URL: {e}")