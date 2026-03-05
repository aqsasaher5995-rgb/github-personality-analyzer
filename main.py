import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("Public repos:", data["public_repos"])
    print("Followers:", data["followers"])
else:
    print("User not found")