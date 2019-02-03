import string
import random
import json
import os
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description="Anti-Phish, an anti-phishing website script")
parser.add_argument('url', help="URL of the target site")
parser.add_argument('-u', '--username', help="The username field of the target site")
parser.add_argument('-p', '--password', help="The password field of the target site")
parser.add_argument('-dl', '--domainlist', help="The email domain list to choose")
args = parser.parse_args()

if not args.url:
    print("Target URL required!")
    parser.print_help()
    sys.exit(1)

if not args.username:
    print("Username field required!")
    parser.print_help()
    sys.exit(1)

if not args.password:
    print("Password field required!")
    parser.print_help()
    sys.exit(1)

if not args.domainlist:
    domain = json.loads(open('domains.json').read())
else:
    domain = json.loads(open('alldomains.json').read())


url = args.url
formusername = args.username
formpassword = args.password

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-+=\|?>.<,'
random.seed = (os.urandom(1024))

name = json.loads(open('names.json').read())

print(flush=True)

while(1):
    nameAdd = ''.join(random.choice(name).lower())
    digitAdd = ''.join(random.choice(string.digits) for i in range(0, 4))
    domainAdd = ''.join(random.choice(domain))

    username = nameAdd + digitAdd + domainAdd
    password = ''.join(random.choice(chars) for i in range(0, 20))

    requests.post(url, allow_redirects=False, data={
        formusername : username,
        formpassword : password
    })

    print("Sending username %s and password %s" % (username, password))
