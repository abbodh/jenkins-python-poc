# script will determine the url to call based on the input ENVIRONMENT which is read by sys.args
from args import argstoparse
import requests

arg = argstoparse()

print("running for environment: " + arg.environment)

api_url = "http://api.open-notify.org/astros.json?env=" + arg.environment
print("hit url: " + api_url)

response = requests.get(api_url)
responseStatusCode = str(response.status_code)
jsonResponse = response.json()

print("status code: " + responseStatusCode)
print("status: " + str(jsonResponse))
