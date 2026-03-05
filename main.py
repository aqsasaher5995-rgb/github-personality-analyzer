import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()

repos = data.get("public_repos")
followers = data.get("followers")
print("Name:", data["name"])
print("Public repos:", repos)
print("Followers:", followers)
print("\nPersonality Analysis")
print("--------------------")
if repos >= 50:
    print("Developer Type: Highly Active Developer")
elif repos >= 10:
    print("Developer Type: Active Developer")
elif repos >=1:
    print("Developer Type: Casual Developer")
else:
    print("Developer Type: Beginner Developer")