# script will determine the url to call based on the input ENVIRONMENT which is read by sys.args
from args import argstoparse
import requests

arg = argstoparse()

print("running for environment: " + arg.environment)

# GET API sample
api_url = "http://api.open-notify.org/astros.json?env=" + arg.environment
print("get api url: " + api_url)

response = requests.get(api_url)
responseStatusCode = str(response.status_code)
jsonResponse = response.json()

print("get response status code: " + responseStatusCode)
print("get response: " + str(jsonResponse))

# POST API sample
post_api_url = "https://jsonplaceholder.typicode.com/posts?env=" + arg.environment
request_body = {
    "title": "foo",
    "body": "bar",
    "userId": 1,
  }

print("post api url: " + post_api_url)
post_response = requests.post(post_api_url, json=request_body)
print("post api response: " + post_response.status_code)
