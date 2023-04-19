import requests
import json

def load_api_keys(file_path):
    with open(file_path, "r") as f:
        keys = json.load(f)
    return keys

keys = load_api_keys("C:\\GitHub\\VoAI\\VoAI\\keys.json")
azure_api_key = keys["azure_api_key"]
azure_region = keys["azure_region"]
openai_api_key = keys["openai_api_key"]

# Set the endpoint URL
endpoint = f"https://{azure_region}.tts.speech.microsoft.com/cognitiveservices/voices/list"

# Set the headers
headers = {
    "Ocp-Apim-Subscription-Key": azure_api_key
}

# Send the GET request to retrieve the list of voices
response = requests.get(endpoint, headers=headers)

# Print the response
print(response.json())
with open("voices.json", "w") as f:
    json.dump(response.json(), f, indent=4)

print("The list of voices has been saved to voices.json")