# Install
- Install python: https://www.python.org/downloads/
- Install the requests library: `pip install -U requests`
- Install pytest unit testing framework: `pip install -U pytest`
- Install pytest html reporter: `pip install pytest-html`

# Pytest HTML
Example to create a self contained HTML report: `pytest *testpath(s)* --html=report.html --self-contained-html` 

# pytest.ini
the `pytest.ini` file is configured to point at the directory that contains the tests.

# Resources
- https://jsonplaceholder.typicode.com/
- https://docs.python-requests.org/en/latest/
- https://docs.pytest.org/en/6.2.x/