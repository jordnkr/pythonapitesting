import requests

patch_url = "https://jsonplaceholder.typicode.com/posts/1"

myobj = {
    'title': 'somevalue',
    'body': 'test body',
    'userId': 1
}

# Verify PATCH status code is 200
def test_patch_posts_status_code_equals_200():
    response = requests.patch(patch_url, data = myobj)
    assert response.status_code == 200

# Verify PATCH response body contains correct 'title' value
def test_patch_posts_title():
    response = requests.patch(patch_url, data = myobj)
    assert response.json()["title"] == "somevalue"