import requests

url = 'https://randomuser.me/api/'
paylod = {
    'results': 5,
    'gender': 'male',
    'nat': ['US', 'GB']
}
r = requests.get(url, paylod)
data = r.json()
print(data)