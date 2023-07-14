# script will determine the url to call based on the input ENVIRONMENT which is read by sys.args
from args import argstoparse
import sys, argparse
import requests

parser = argparse.ArgumentParser()
args=parser.parse_args()

print("running for environment: " + args.environment)

print("hit url: " + api_url)
api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)
responseStatusCode = str(response.status_code)
jsonResponse = response.json()

print("status code: " + responseStatusCode)
print("status: " + str(jsonResponse))
