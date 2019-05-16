import requests

response = requests.get('http://www.cookiepool.com/random/github')

print(response.text)