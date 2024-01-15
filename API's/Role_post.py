import requests
import json

base_url = "https://api.qa.bapsapps.org/mds/roles"

payload = {
    "startDate": "2019-08-24T14:15:22Z",
    "endDate": "2019-08-24T14:15:22Z",
    "status": "string",
    "roleTypeId": 392,
    "code": "string",
    "uucode": "string",
    "name": "string",
    "uuname": "string",
}

headers = {"Content-Type": "application/json", "Accept": "application/json"}

response = requests.request("POST", base_url, json=payload, headers=headers)

if response.status_code == 200:
    try:
        # Attempt to parse the response JSON and print it
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content directly



