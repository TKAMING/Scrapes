#!/usr/bin/python
# by Tobas Karuth (TKAMING)

# imports
import os
import sys
from .twittermodule import twitterScrape

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
            -v, --version ------------- Scrapes Version
            -h, --help  --------------- Help Menu

        [+] Example:
            scrapes [ARGUMENT]
"""

# option menu
options_menu = """
        [+] Command and Control:
            [twitter] ---------------- To scrape Twitter

        [+] Options:
            [help] ------------------- Help Menu
            [version] ---------------- Version Number
            [update] ----------------- Update Scrape
            [clear] ------------------ Clears the screen
            [quit] ------------------- Quit

        [*] Select an [option]...
"""

header = f"[~] scrapes $ " # sets up user input interface


# clear screen
def clear():
    os.system("clear")

# command line interface
def cli():
    # display banner
    clear()
    print(banner)

    # loop user input
    while True:

        # user input, option
        option = input(header)

        # command options
        if option == "help":
            print(banner)
            print(options_menu)

        elif option == "clear":
            print(banner)
            clear()

        #elif option == "version":

        #elif option == "update":

        elif option == "quit" or option == "exit":
            print("\n[*] Exiting...")
            sys.exit()

        elif option == "twitter":
            search = input("[*] For what keyword to scrape twitter through?\n")
            twitterScrape(search)

# main code
def main():
    # checks for arguments
    try:
        args = sys.argv[1]
    except IndexError:
        print("""
                [*] Argument doesn´t exist, try --help.
                    Usage: scrapes [ARGUMENT]
        """)
    else:

        if args == "run":
            # run command line interface
            cli()

        elif args == "--version" or args == "-v":
           print(banner) 

        elif args == "--help" or args == "-h":
            print(help_menu)

        else:
            print("[*] Error")


# runs main code
if __name__ == "__main__":
    # runs main function
    main()
