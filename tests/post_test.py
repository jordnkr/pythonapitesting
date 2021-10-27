import requests

post_url = "https://jsonplaceholder.typicode.com/posts"

myobj = {
    'title': 'somevalue',
    'body': 'test body',
    'userId': 1
}

# Verify POST response status code is correct
def test_post_posts_status_code_equals_201():
    response = requests.post(post_url, data = myobj)
    assert response.status_code == 201
    
# Verify POST response body contains correct 'id' value
def test_post_posts_response_id():
    response = requests.post(post_url, data = myobj)
    assert response.json()["id"] == 101