## BASIC IMPORT ##

import requests

# Import data for a specific Lego colour
url = 'https://rebrickable.com/api/v3/lego/colors/20/?key=<api_key>'
response = requests.get(url)

# Print the json
print(response.text)

# Step through each internal key, value pair in the json
json_data = response.json()
for key, value in json_data.items():
    if key != 'external_ids':
        print(key + ': ', value)

# Get information about the request (status, content type of the reponse, etc)
print(response.status_code)
print(response.headers['Content-Type'])
print(response.headers['Content-Encoding'])
print(response.headers['last-modified'])


## IMPORT USING PARAMETERS ##

query_parmeters = {'key': '<api_key>'}
response_params = requests.get(
    'https://rebrickable.com/api/v3/lego/colors/20/', params=query_parmeters)

# Print the json
print(response_params.text)
