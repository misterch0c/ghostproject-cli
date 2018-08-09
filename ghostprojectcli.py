#!/usr/bin/env python
# Author = @misterch0c

import requests
import time 
import argparse

parser = argparse.ArgumentParser(description="Try to retrieve password for email address from ghostproject.fr")
parser.add_argument("-a", dest="address",
                  help="Single email address to be checked")
parser.add_argument("-f", dest="filename",
                  help="File to be checked with one email addresses per line")
args = parser.parse_args()
server = "https://ghostproject.fr/"  
OKGREEN = '\033[92m'
FAILRED = '\033[91m'
address = str(args.address)
filename = str(args.filename)


ghost=r"""
       .-.
      ( " )
   /\_.' '._/\
   |         |
    \       /
     \    /`
   (__)  /
   `.__.'

"""
def main():
    print(ghost)
    if address != "None":
        checkAddress(address)
    elif filename != "None":
        email = [line.rstrip('\n') for line in open(filename)]
        for email in email:
            checkAddress(email)


def checkAddress(email):
    check = requests.post(server+"search.php",data={'param':email})
    rez=check.text.split('\\n')

    if str(check.status_code) == "200":
        if "No results found" in check.text:
            print FAILRED + "Nothing found"
            return False
        else:

            for result in rez[1:-1]:
                print OKGREEN+result
            return True


if __name__ == "__main__":
    main()
