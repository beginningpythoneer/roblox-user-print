import requests

def username_to_user_id(username: str): # cannot finish, roblox keeps returning empty data
    payload = {
        "usernames": [
            username
        ],
        "excludeBannedUsers": False
    }

    resp = requests.post("https://users.roblox.com/v1/usernames/users", data=payload).json()

    return resp

def get_user_info(user_id: int):
    resp = requests.get(f"https://users.roblox.com/v1/users/{user_id}")

    if resp.status_code == 200:
        return resp.json()
    else:
        return None