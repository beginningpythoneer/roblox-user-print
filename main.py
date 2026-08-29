from dataclasses import dataclass # Made by AI
from argparse import ArgumentParser
from modules import api
from colorama import Fore, Back, Style

parser = ArgumentParser()

parser.add_argument("-u", "--userid", dest = "user_id", help = "Target UserID")

@dataclass
class UserProfile: # Made by AI
    username: str
    display_name: str
    registration_date: str
    is_verified: bool
    is_banned: bool
    description: str

def print_user_data(user: UserProfile):
    print(f"{Style.BRIGHT}{user.display_name} {(f"{Back.BLUE}✔ {Style.RESET_ALL} ") if user.is_verified else ""}{Back.LIGHTRED_EX+Style.BRIGHT}{(" Banned ") if user.is_banned else ""}{Style.RESET_ALL}")
    print(f"{Style.DIM}@{user.username} {Style.RESET_ALL}")
    print(f"Registered at {user.registration_date.replace("-", ".").split("T")[0]} {user.registration_date.split("T")[1]}")
    print("")
    print(f"{Style.DIM}{user.description}{Style.RESET_ALL}")

def main():
    args = parser.parse_args()

    try:
        user_data = api.get_user_info(int(args.user_id))

        username = user_data.get("name")
        display_name = user_data.get("displayName")
        reg_date = user_data.get("created")
        is_verified = user_data.get("hasVerifiedBadge")
        is_banned = user_data.get("isBanned")
        desc = user_data.get("description")

        user = UserProfile(username, display_name, reg_date, is_verified, is_banned, desc)

        print_user_data(user)
    except ValueError: # Made by AI
        print("User ID must be a valid number.")
    except TypeError:
        print("Looks like you forgot to put the argument. Usage: python main.py -u userid")

if __name__ == "__main__":
    main()