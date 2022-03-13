import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, dest='url', help='Asset post url like: https://smartbeans-domain.tld/api/admin/asset')
parser.add_argument('-a', '--admin-api-key', type=str, dest='api_key', help='Authorization admin api key')
parser.add_argument('-d', '--data', type=str, dest='data', help='JSON file with asset meta data')

args = parser.parse_args()

with open(args.data, "r") as fp:
  assets = json.load(fp)

for asset in assets:
  response = requests.post(args.url, json=asset, headers={"Authorization": f"Bearer {args.api_key}", "Content-type": "application/json"})
  print(response.text)
