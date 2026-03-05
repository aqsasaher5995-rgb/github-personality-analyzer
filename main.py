import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Public repos:", data["public_repos"])
print("Followers:", data["followers"])