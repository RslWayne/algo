import requests
url = 'https://api.github.com/repos/risification/django_project3/commits?page=1&per_page=100'
response = requests.get(url).json
  