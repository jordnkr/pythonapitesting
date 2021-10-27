import requests

delete_url = "https://jsonplaceholder.typicode.com/posts/1"

# Verify DELETE response code is correct
def test_delete_posts_status_code_equals_200():
	response = requests.delete(delete_url)
	assert response.status_code == 200