"""

requests:

. Es una librería Python que facilita el trabajo con peticiones HTTP
. Instalación: pip install requests

"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/", verify=False)
print(response.text)
print(response.status_code)
print(response.encoding)
print(response.headers)

param = {'postId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/comments', params=param, verify=False)
print(response.text)

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', params=data, verify=False)
print(response.status_code)

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', params=data, verify=False)
print(response.status_code)

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1', verify=False)
print(response.status_code)
