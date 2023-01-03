# by Tobias Karuth (TKAMING)

from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

def twitterScrape():
    name = "Twitter"

    username = input(f"[*] Whats your {name} account username (Valid)?\n")
    password = input(f"[*] Whats your {name} account password (Valid)?\n")
    email = input(f"[*] Whats your {name} account E-mail (Valid)?\n")


    n = int(input("[*] How many kewords do you have?\n"))
    search = []
    print(f"What keyword {name} to scrape through?")

    for i in range(1, n+1):
        keyword = input(f"{i}. Keyword: ")
        search.append(keyword)

    print(f"Scrape in {name} for: {search}\n")


    option = input("[~] Do you want to have a Interval [y/n]\n").lower()

    if option == "y" or option == "yes":
        print("[*] Example: yyyy-mm-dd")
        since = input("Since: ")
        until = input("Until: ")
        interval = 1
# TODO Error not NONE must arg 1 must be str
    else:
        since = None
        until = None
        interval = None

    
    option = input("""
            [~] In which order to sort by the Tweets?

            [+] Options:
                1) Top --------- to display the most trending Tweets
                2) Latest ------ to display the latest posted Tweets
    \n""")

    if option == "1":
        display_type = "Top"

    elif option == "2":
        display_type = "Latest"

    else:
        print("[*] Incorrect answer! So Top sort has been choosen automaticly\n")


    lang = input(""""
            [~] Which language you want to use?

            [*] Example:
                en ---------- for English
                de ---------- for German
                and so forth
    \n""").lower()


    option = input("""
            [~] Do you want to use a geocode to scrape Tweets geolocated
                less than 200 km (depending on your input) 
                from your entered geolocation?

            [*] Example:
                no --------------------------------- use no geolocation
                example: 38.3452,-0.481006,200km --- for less than 200km from Alicante (Spain) Lat=38.3452, Long=-0.481006
    \n""").lower()

    if option == "n" or option =="no":
        geocode = None

    else:
        geocode = option


    #scraping process
    data = scrape(words=[search], since=since, until=until, from_account=None, interval=interval,
                  headless=False, display_type=display_type, save_images=False, lang=lang,
                  resume=False, filter_replies=False, proximity=False, geocode=geocode)

    data = scrape(hashtag="bitcoin", since="2021-08-05", until="2021-08-08", from_account=None, interval=interval,
                  headless=True, display_type=display_type, save_images=True,
                  resume=False, filter_replies=True, proximity=True)

    # Get the main information of a given list of users
    users = users

    # this function return a list that contains : 
    # ["nb of following","nb of followers", "join date", "birthdate", "location", "website", "description"]
    users_info = get_user_information(users, headless=True)

    env_path = ".env"

    following = get_users_following(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)
    followers = get_users_followers(users=users, env=env_path, verbose=0, headless=True, wait=1, limit=50, file_path=None)

twitterScrape()
