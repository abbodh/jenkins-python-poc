
#script will determine the url to call based on the input ENVIRONMENT
import requests
api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)
responseStatusCode = str(response.status_code)
jsonResponse = response.json()
print("url: " + api_url)
print("status code: " + responseStatusCode)
print("status: " + jsonResponse)
