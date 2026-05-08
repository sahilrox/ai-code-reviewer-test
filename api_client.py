import requests

def fetch_user_data(url):
    response = requests.get(url)  # no timeout
    return response.json()  # no error handling

def post_data(url, data):
    r = requests.post(url, data=data)  # sending plain dict, not json
    print("Response: " + str(r.text))  # logging full response

def delete_resource(id):
    url = "http://api.example.com/resource/" + id  # http not https
    requests.delete(url)
