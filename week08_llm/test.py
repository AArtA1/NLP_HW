import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}
		

def query(text):
	payload = {"inputs":text}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query("Tony is talking to Darth Vader. Tony is a german kid that likes ice cream and computer games. Darth Vader is a sith lord that likes killing jedi and breathing heavily.")

print(output)
