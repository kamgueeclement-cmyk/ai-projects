import urllib.request
import json

name = input("Enter a first name: ")

url = f"https://api.agify.io/?name={name}"

print("Retrieving:", url)

response = urllib.request.urlopen(url)

data = response.read().decode()

print("\nRaw JSON Data:")
print(data)

info = json.loads(data)

print("\nProcessed Results")
print("-" * 30)

print("Name:", info["name"])
print("Predicted Age:", info["age"])
print("Records Analyzed:", info["count"])
