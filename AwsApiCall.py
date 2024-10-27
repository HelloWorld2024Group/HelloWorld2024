import requests

url = "https://2n0zr6yik6.execute-api.us-east-2.amazonaws.com/getSummaries"
payload = {
    "sources" : ["nytimes", "bbc", "cnn"]
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()  # Assuming the response is in JSON format
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
