import json
import requests
from io import StringIO

api_token = ''
api_token = ''
api_base_url = ''

headers = {
    'accept': 'application/json','Authorization': 'Bearer {0}'.format(api_token),
        }

def get_api_info():

    api_url = '{0}Labels'.format(api_base_url)
    api_url = api_base_url
    response = requests.get(api_url, verify=False, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

api_info = get_api_info()

for item in api_info:
    print(" ")
    print ("Id:", item["Id"])
    print("Names:", item["Names"])
    print("Image:", item["Image"])
    print("ImageID:", item["ImageID"])
    print("Labels:", item["Labels"])
    print("State:", item["State"])
    print("Status:", item["Status"])
