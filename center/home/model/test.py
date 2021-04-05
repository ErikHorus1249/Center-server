import requests
import json

HASH_CODE = '6609c54462c3abb7f1f92e0d5a52017bfc28c765cd170cc9548072a43a551b52'
def test():
    response = requests.get("http://localhost:8080/home/", params={'q':HASH_CODE},)
    data = json.loads(response.text)
    return data['link']

def post_model(model_hash):
    response = requests.post("http://localhost:8080/home/",json={'hash':'test'})
    # json_response = response.json()
    return response

print(test())