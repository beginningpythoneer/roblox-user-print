from argparse import ArgumentParser
from modules import api
from colorama import Fore, Back, Style

parser = ArgumentParser()

parser.add_argument("-u", "--userid", dest = "user_id", help = "Target UserID")

def print_user_data(username: str, display_name: str, registration_date: str, is_verified: bool, is_banned: bool, description: str):
    print(f"{Style.BRIGHT}{display_name} {(f"{Back.BLUE}✔ {Style.RESET_ALL} ") if is_verified else ""}{Back.LIGHTRED_EX+Style.BRIGHT}{(" Banned ") if is_banned else ""}{Style.RESET_ALL}")
    print(f"{Style.DIM}@{username} {Style.RESET_ALL}")
    print(f"Registered at {registration_date.replace("-", ".").split("T")[0]} {registration_date.split("T")[1]}")
    print("")
    print(f"{Style.DIM}{description}{Style.RESET_ALL}")

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

        print_user_data(username, display_name, reg_date, is_verified, is_banned, desc)
    except Exception as ex:
        if isinstance(ex, TypeError):
            print("You probably didnt specify the target UserID. Usage: py main.py -u userId")
        else:
            print(f"Unexpected error! {ex}")

if __name__ == "__main__":
    main()