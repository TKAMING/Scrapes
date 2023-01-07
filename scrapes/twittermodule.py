# by Tobias Karuth (TKAMING)

import os
import sys
import getpass
import time
import csv
import dotenv
from dotenv import load_dotenv
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

def twitterScrape():
    try:
        username = getpass.getuser() # gets username
        header = f"[~] {username}@scrapes $ " # sets up user input interface
        name = "Twitter"
        print("[+] Starting Twitter scraping process...\n")

        time.sleep(1)
        os.system("clear")

        n = int(input(f"[*] How many kewords do you have?\n $ "))
        search = []
        print(f"\nWhat keyword {name} to scrape through?")

        for i in range(1, n+1):
            keyword = input(f"{i}. Keyword: ")
            search.append(keyword)

        print(f"Scrape in {name} for: {search}\n")

        time.sleep(2)
        os.system("clear")

        print("[~] You need to enter an Interval\n    Example: yyyy-mm-dd\n")
        since = input("Since: ")
        until = input("Until: ")
        interval = 1

        time.sleep(1)
        os.system("clear")

        option = input(f"""
[~] In which order to sort by the Tweets?

[+] Options:
    1) Top --------- to display the most trending Tweets
    2) Latest ------ to display the latest posted Tweets
        \n{header}""").lower()

        if option == "1" or option == "top":
            display_type = "Top"

        elif option == "2" or option == "latest":
            display_type = "Latest"

        else:
            print("[*] Incorrect answer! So Top sort has been choosen automaticly")
            display_type = "Top"

        time.sleep(1)
        os.system("clear")

        lang = input(f"""
[~] Which language you want to use?

[*] Example:
    en ---------- for English
    de ---------- for German
    fr ---------- for French
    and so forth...
        \n{header}""").lower()

        time.sleep(1)
        os.system("clear")

        option = input(f"""
[~] Do you want to use a geocode to scrape Tweets geolocated
    less than 200 km (depending on your input) 
    from your entered geolocation?
    
[*] Example:
    no --------------------------------- use no geolocation
    example: 38.3452,-0.481006,200km --- for less than 200km from Alicante (Spain) Lat=38.3452, Long=-0.481006
        \n{header}""").lower()

        if option == "n" or option =="no":
            geocode = None

        else:
            geocode = option

    except:
        print("[*] Error: Exiting...")
        sys.exit()

    # scraping process
    data = scrape(words=search, since=since, until=until, from_account=None, interval=interval,
                  headless=False, display_type=display_type, save_images=True, lang=lang,
                  resume=False, filter_replies=False, proximity=False, geocode=geocode)


def twitterUserInfo():
    name = "Twitter"
    try:
        username = input(f"[*] Whats your {name} account username (Valid)?\n $ ")

        # password validation

        while True:
            password = getpass.getpass(prompt = f"\n[*] Whats your {name} account password (Valid)?\n $ ")
            password_check = getpass.getpass(prompt = f"\n[*] Enter your password again\n $ ")

            if password == password_check:
                print("\n[+] Correct...\n")
                break

            else:
                print("The passwords are not the same. Try again...\n")
                time.sleep(2)
                os.system("clear")
                continue

        email = input(f"\n[*] Whats your {name} account E-mail (Valid)?\n $ ")

        # Get the main information of a given list of users
        n = int(input(f"\n[*] How many users do you want to get the information from?\n $ "))
        users = []
        print("\nKnow enter the usernames")

        for i in range(1, n+1):
            usernames = input(f"{i}. Usernames: ")
            users.append(usernames)

        print(f"Search for this list of User {users}\n")

        time.sleep(2)
        os.system("clear")

    except:
        print("\n[*] Error: Exiting...")
        sys.exit()

    env_path = ".env"
    dotenv_file = dotenv.find_dotenv()
    load_dotenv(dotenv_path=env_path)

    # Write changes to .env file
    os.environ["SCWEET_EMAIL"] = email
    dotenv.set_key(dotenv_file, "SCWEET_EMAIL", os.environ["SCWEET_EMAIL"])
    os.environ["SCWEET_PASSWORD"] = password
    dotenv.set_key(dotenv_file, "SCWEET_PASSWORD", os.environ["SCWEET_PASSWORD"])
    os.environ["SCWEET_USERNAME"] = username
    dotenv.set_key(dotenv_file, "SCWEET_USERNAME", os.environ["SCWEET_USERNAME"])

    # this function return a list that contains : 
    # ["nb of following","nb of followers", "join date", "birthdate", "location", "website", "description"]
    users_info = get_user_information(users, headless=True)


    following = get_users_following(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)
    followers = get_users_followers(users=users, env=env_path, verbose=0, headless=True, wait=1, limit=50, file_path=None)

    print(users_info)
    print(following)
    print(followers)


def readScrapedData():
    print("[*] What file you want to read? All files:")
    opt_files = os.listdir(path="~/outputs/")
    print(opt_files)
    file = input(" $ ")

    # opens the file
    reader = csv.reader(open("~/outputs/" + file, "r"))
    data = []
    for line in reader:
        data.append(line)

    header = data.pop(0)

    # prints the table of the .csv data
    # print header table
    print("#" * 220)
    print(" # ", end="  ")
    for column in header:
        print(fixed_length(column,20), end= " # ")
    print()
    print("#" * 220)

    # print main table
    for line in data:
        print(" # ", end="  ")
        for column in line:
            print(fixed_length(column,20), end= " # ")
        print()
    print("#" * 220)



def fixed_length(text, length):
    if len(text) > length:
        text = text[:length]

    elif len(text) < length:
        text = (text + " " * length)[:length]
    
    return text
