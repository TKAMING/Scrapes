#!/usr/bin/python
# by Tobas Karuth (TKAMING)

# imports
import os
import sys

# banner for display
banner = """


                    [::] "Scrapes" the hole Internet... [::]
                      [::] Created By : Tobias Karuth [::]
"""

# help menu
help_menu = """
        [+] Arguments:
            -r, --run ----------------- Run Scrapes
            -v, --version ------------- Scrapes Version
            -h, --help  --------------- Help Menu

        [+] Usage:
            scrapes [ARGUMENT]
"""

header = f"[~] scrapes $ " # sets up user input interface


# clear screen
def clear():
    os.system("clear")

# command line interface
def cli(arguments):
    # display banner
    clear()

    print(banner)

# main code
def main():
    # checks for arguments
    #try:
    args = sys.argv[:1]
    #except IndexError:
    #    arguments_exist = False
    #else:
    #    arguments_exist = True

    if args == "--run" or args == "-r":
        # run command line interface
        cli()
    
    elif args == "--version" or args == "-v":
       print(banner) 

    elif args == "--help" or args == "-h":
        print(help_menu)

# runs main code
if __name__ == "__main__":
    # runs main function
    main()
