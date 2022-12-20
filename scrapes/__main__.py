#!/usr/bin/python
# by Tobas Karuth (TKAMING)

# imports
import os
import sys
from datetime import datetime

# banner for display
banner = """


                    [::] "Scrapes" the hole Internet... [::]
                      [::] Created By : Tobias Karuth [::]
"""

# help menu
help_menu = """
        [+] Arguments:
            
        [+] Example:
            scrapes ...
"""


# clear screen
def clear():
    os.system("clear")

# terminates program
def exit():
    print("\n[*] Exiting...")
    sys.exit()

# gets current date and time
def current_date():
    current = datetime.now()    

    return current.strftime("%m-%d-%Y_%H-%M-%S")

# update OnlyRAT
def update():

    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system(f"curl https://raw.githubusercontent.com/TKAMING/Scrapes/main/version.txt | tee ~/.Scrapes/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{local_path}/version.txt", "r").read())
    latest_version = float(open(f"{local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("rm -rf ~/.Scrapes/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print("[~] Update Scrapes? [y/n]\n")

        # user input, option
        option = input(f"{header}")
        
        # update
        if option == "y":
            os.system(f"bash ~/.Scrapes/payloads/update.sh")

        # exception
        # else:
        #     main()

    # otherwise, run main code
    else:
        print("\n[+] Scrapes already up to date")
        print("[*] Hit any key to continue...\n")
        input(header)

# command line interface
def cli(arguments):
    # display banner
    clear()

    print(banner)

    # if arguments exist
    if arguments:

        argument = sys.argv[1]

        if argument.endswith(".rat"):
            print("\t[~] Type \"help\" for help menu :\n")

            # loop user input
            while True:

                # user input, option
                option = input(header)
                rat_file = argument

# main code
def main():
    
    # clear screen
    clear()

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    # run command line interface
    cli(arguments_exist)

# runs main code
if __name__ == "__main__":
    # runs main function
    main()
