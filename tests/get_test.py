import requests

get_url = "https://jsonplaceholder.typicode.com/posts/1"

# Verify GET response code is correct
def test_get_posts_status_code_equals_200():
	response = requests.get(get_url)
	assert response.status_code == 200

# Verify GET content type is expected type
def test_get_posts_content_type_equals_json():
	response = requests.get(get_url)
	assert response.headers["Content-Type"] == "application/json; charset=utf-8"