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
    print("\nPersonality Analysis")
print("--------------------")

repos = data.get("public_repos")
followers = data.get("followers")

if repos > 50:
    print("Developer Type: Highly Active Open Source Contributor")
elif repos > 10:
    print("Developer Type: Active Developer")
else:
    print("Developer Type: Beginner Developer")

if followers > 1000:
    print("Influence Level: High")
elif followers > 100:
    print("Influence Level: Medium")
else:
    print("Influence Level: Growing")

