import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nGitHub Profile")
    print("-------------------")
    print("Name:", data.get("name"))
    print("Public repos:", data.get("public_repos"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))
    print("Location:", data.get("location"))

else:
    print("User not found")