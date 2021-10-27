import requests

put_url = "https://jsonplaceholder.typicode.com/posts/1"

myobj = {
    'title': 'somevalue',
    'body': 'test body',
    'userId': 1
}

# Verify PUT status code is 200
def test_put_posts_status_code_equals_200():
    response = requests.put(put_url, data = myobj)
    assert response.status_code == 200

# Verify PUT response body contains correct 'title' value
def test_put_posts_title():
    response = requests.put(put_url, data = myobj)
    assert response.json()["title"] == "somevalue"