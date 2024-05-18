"""

requests:

. Es una librería Python que facilita el trabajo con peticiones HTTP
. Instalación: pip install requests

"""

import requests


def test_status_code_200():
    response = requests.get('https://api.github.com', verify=False)
    assert response.status_code == 200

def test_status_code_404():
    response = requests.get('https://api.github.com/pepe', verify=False)
    assert response.status_code == 404

def test_length_text():
    response = requests.get('https://api.github.com', verify=False)
    assert len(response.text) > 1000

def test_encoding():
    response = requests.get('https://api.github.com', verify=False)
    assert response.encoding == 'utf-8'

def test_headers():
    response = requests.get('https://api.github.com', verify=False)
    assert response.headers['Content-Length'] == '496'

def test_titles_no_empty():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', verify=False)
    data = response.json()
    for d in data:
        assert len(d['title']) > 0

def test_count_comments_by_id():
    param = {'postId': 1}
    response = requests.get('https://jsonplaceholder.typicode.com/comments', params=param, verify=False)
    assert len(response.json()) == 5

def test_post():
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', params=data, verify=False)
    assert response.status_code == 200

def test_put():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', verify=False)
    cant_posts = len(response.json())
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    requests.put('https://jsonplaceholder.typicode.com/posts', params=data, verify=False)
    response = requests.get('https://jsonplaceholder.typicode.com/posts', verify=False)
    assert len(response.json()) == (cant_posts + 1)