import requests

response = requests.get('http://api.open-notify.org/astros.json')
print(response.json())
print('The people currently in space are:')
for people in response.json().get('people'):
    print(people.get('name'))

