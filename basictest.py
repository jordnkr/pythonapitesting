import requests

def test_get_posts_check_status_code_equals_200():
     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
     assert response.status_code == 200