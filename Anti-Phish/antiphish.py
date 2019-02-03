import argparse
import json
import os
import random
import string
import sys

import requests

# Copyright 2019 Kixiron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    domain = json.loads(open('data/domains.json').read())
else:
    domain = json.loads(open('data/alldomains.json').read())


url = args.url
formusername = args.username
formpassword = args.password

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-+=\|?>.<,'
random.seed()

name = json.loads(open('data/names.json').read())

print(flush=True)

entry_num = 0
while(1):
    entry_num += entry_num
    nameAdd = ''.join(random.choice(name).lower())
    digitAdd = ''.join(random.choice(string.digits) for i in range(0, 4))
    domainAdd = ''.join(random.choice(domain))

    username = nameAdd + digitAdd + domainAdd
    password = ''.join(random.choice(chars) for i in range(0, 20))

    requests.post(url, allow_redirects=False, data={
        formusername : username,
        formpassword : password
    })

    print("Sending username {} and password {} | Entry #{}".format(username, password, entry_num))
