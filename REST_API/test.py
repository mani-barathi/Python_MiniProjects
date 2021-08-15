import requests        # pip install requests

# this is a test script to test the API

# get all movies
# res = requests.get('http://127.0.0.1:5000/movie')

# get specific movie by id
res = requests.get('http://127.0.0.1:5000/movie/2')

# add a new movie by passing in name
# res = requests.post('http://127.0.0.1:5000/movie/add',json={"name":"titanic"})

# like a movie based on id
# res = requests.post('http://127.0.0.1:5000/movie/like',json={"id":6})

print(f'status code: {res.status_code}')
# print(f'headers: {res.headers}')
print(f'data:',res.json())