import requests

def test_get_posts_check_status_code_equals_200():
     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
     assert response.status_code == 200

def test_get_posts_check_content_type_equals_json():
     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
     assert response.headers["Content-Type"] == "application/json; charset=utf-8"