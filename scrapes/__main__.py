#!/usr/bin/python
# by Tobas Karuth (TKAMING)

# imports
import os
import sys
import getpass
import readline
from .twittermodule import twitterScrape, twitterUserInfo,readScrapedData

# banner for display
banner = """
        
          sSSs    sSSs   .S_sSSs     .S_SSSs     .S_sSSs      sSSs    sSSs  
         d%%SP   d%%SP  .SS~YS%%b   .SS~SSSSS   .SS~YS%%b    d%%SP   d%%SP  
        d%S'    d%S'    S%S   `S%b  S%S   SSSS  S%S   `S%b  d%S'    d%S'    
        S%|     S%S     S%S    S%S  S%S    S%S  S%S    S%S  S%S     S%|     
        S&S     S&S     S%S    d*S  S%S SSSS%S  S%S    d*S  S&S     S&S     
        Y&Ss    S&S     S&S   .S*S  S&S  SSS%S  S&S   .S*S  S&S_Ss  Y&Ss    
        `S&&S   S&S     S&S_sdSSS   S&S    S&S  S&S_sdSSS   S&S~SP  `S&&S   
          `S*S  S&S     S&S~YSY%b   S&S    S&S  S&S~YSSY    S&S       `S*S  
           l*S  S*b     S*S   `S%b  S*S    S&S  S*S         S*b        l*S  
          .S*P  S*S.    S*S    S%S  S*S    S*S  S*S         S*S.      .S*P  
        sSS*S    SSSbs  S*S    S&S  S*S    S*S  S*S          SSSbs  sSS*S   
        YSS'      YSSP  S*S    SSS  SSS    S*S  S*S           YSSP  YSS'    
                        SP                 SP   SP                          
                        Y                  Y    Y                           
                                                                    
                    [::] "Scrapes" the hole Internet... [::]
                      [::] Created By : Tobias Karuth [::]
"""

# help menu
help_menu = """
        [+] Arguments:
            run ----------------------- Run Scrapes
            install + [NAME] ---------- Install something
            -v, --version ------------- Scrapes Version
            -h, --help  --------------- Help Menu

        [+] Names:
            chrome-driver ------------- to install the Chrome driver    

        [+] Example:
            scrapes [ARGUMENT]
"""

# option menu
options_menu = """
        [+] Command and Control:
            [twitter scrape] ---------------- To scrape Twitter
            [twitter user info] ------------- To enter a list of User and get their information via Twitter

        [+] Options:
            [help] ------------------- Help Menu
            [version] ---------------- Version Number
            [update] ----------------- Update Scrape
            [uninstall] -------------- Unistalls Scrape
            [install] + [NAME] ------- Install something
            [read data] -------------- Reads scraped data
            [clear] ------------------ Clears the screen
            [quit] ------------------- Quit

        [*] Select an [option]...
"""

username = getpass.getuser() # gets username
header = f"[~] {username}@scrapes $ " # sets up user input interface
remote_path = "raw.githubusercontent.com/TKAMING/Scrapes/main" # url path for Scrapes files
local_path = f"/home/{username}/.Scrapes" if username != "root" else "/root/.Scrapes" # gets path of Scrapes

# clear screen
def clear():
    os.system("clear")

# update Scrapes
def update():
    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system(f"sudo curl https://raw.githubusercontent.com/TKAMING/Scrapes/main/version.txt | tee ~/.Scrapes/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{local_path}/version.txt", "r").read())
    latest_version = float(open(f"{local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("sudo rm -rf ~/.Scrapes/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print("[~] Update Scrapes? [y/n]\n")

        # user input, option
        option = input().lower()
        
        # update
        if option == "y" or option == "yes":
            os.system(f"bash ~/.Scrapes/update.sh")

    else:
        print("\n[+] Scrapes already up to date")
        print("[*] Hit any key to continue...\n")
        input(header)
        
def remove():
    # confirmation
    print("\n[~] Are you sure you want to remove Scrapes [y/n]\n")

    # user input
    option = input().lower()

    # delete Scrapes
    if option == "y" or option == "yes":
        os.system("sudo rm -rf ~/.Scrapes")
        print("[*] Scrapes successfully uninstalled and exeting. Bye...")
        sys.exit()

    # cancel
    if option == "n" or option == "no":
        main()


# command line interface
def cli():
    # display banner
    clear()
    print(banner)

    # loop user input
    while True:

        # user input, option
        option = input(header).lower()

        # command options
        if option == "help":
            clear()
            print(banner)
            print(options_menu)

        elif option == "clear":
            print(banner)
            clear()

        elif option == "version":
            os.system(f"sudo cat {local_path}/version.txt")

        elif option == "update":
            update()
            exit()

        elif option == "quit" or option == "exit":
            print("\n[*] Exiting...")
            sys.exit()

        # remove installation
        elif option == "remove" or option == "uninstall":
            remove()

        elif option == "twitter scrape":
            twitterScrape()

        elif option == "twitter user info":
            twitterUserInfo()

        elif option == "read data":
            readScrapedData()

        # exception
        else:
            os.system(option)
        
        # new line for cleaner UI
        print("\n")

# main code
def main():
    # checks for arguments
    try:
        args = sys.argv[1]
    except IndexError:
        print("""
                [*] Argument doesn??t exist, try --help.
                    Usage: scrapes [ARGUMENT]
        """)
    else:

        if args == "run":
            # run command line interface
            cli()

        elif args == "--version" or args == "-v":
           os.system(f"cat {local_path}/version.txt")

        elif args == "--help" or args == "-h":
            print(help_menu)

        #elif args == "install chrome-driver":
        #    # confirmation
        #    print("\n[~] Are you sure you want to install the Chrome driver [y/n]\n")
        #    # user input
        #    option = input().lower()

        #    if option == "y" or option == "yes":
        #        os.system("bash chrome_driver_install.sh")
        #    else:
        #        print("[*] Cancel...")

        else:
            print("[*] Error")


# runs main code
if __name__ == "__main__":
    # runs main function
    main()
