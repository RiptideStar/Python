import requests #pip install requests
import sys

print("--- Command Line:", sys.argv)
# print(len(sys.argv))
if len(sys.argv) < 2:
    #expect an argument past the python file
    print(f"Usage: {sys.argv[0]} full_long_url [short_name]")
    exit(1)

#get URL that we want to shorten
url = sys.argv[1]

#unique to an individual's cuttly account
api_key = "160d03c1a395a524f253d757a8dc84f33d3f5"

if len(sys.argv) >= 3:
    #at this point, the user provided a short name
    short_name = sys.argv[2]
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={short_name}"
else:
    #at this point, user didn't provide a short name
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

print("--- api_url:", api_url)

# make the request
response = requests.get(api_url)
print("--- response:", response)
print("--- response.json:", response.json())

data = response.json()["url"]
print("--- data:", data)

if data['status'] == 7:
    #Success, link has been shortened
    shortened_url = data["shortLink"]
    print("--- Shortened URL:", shortened_url)
else:
    print("Error shortening URL:", data)