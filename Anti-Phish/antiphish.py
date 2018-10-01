import string
import random
import json
import os
import requests
import argparse

parser = argparse.ArgumentParser(description="Anti-Phish, an anti-phishing website script")
parser.add_argument('url', dest="urlField", help="URL of the target site")
parser.add_argument('-u', '--username', dest="usernameField", help="The username field of the target site")
parser.add_argument('-p', '--password', dest="passwordField", help="The password field of the target site")
parser.add_argument('-dl', '--domainlist', dest="domainList", help="The email domain list to choose")
args = parser.parse_args()

if not args.urlField:
    print("Target URL required!")
    parser.print_help()
    sys.exit(1)

if not args.usernameField:
    print("Username field required!")
    parser.print_help()
    sys.exit(1)

if not args.passwordField:
    print("Password field required!")
    parser.print_help()
    sys.exit(1)

if not args.domainList:
    domain = json.loads(open('domains.json').read())
else:
    domain = json.loads(open('alldomains.json').read())


url = args.urlField
formusername = args.usernameField
formpassword = args.passwordField

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-+=\|?>.<,'
random.seed = (os.urandom(1024))

name = json.loads(open('names.json').read())

while(1):
    nameAdd = ''.join(random.choice(name).lower())
    digitAdd = ''.join(random.choice(numbers) for i in range(0, 4))
    domainAdd = ''.join(random.choice(domain))

    username = nameAdd + digitAdd + domainAdd
    password = ''.join(random.choice(chars) for i in range(0, 20))

    requests.post(url, allow_redirects=False, data={
        formusername: username
        formpassword: password
    })

    print("Sending username %s and password %s" % (username, password))
