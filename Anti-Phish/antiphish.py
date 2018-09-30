import string
import random
import json
import os
import requests

url = 'INSERT_SITE_URL'
usernameField = 'INSERT_PASSWORD_FIELD'
passwordField = 'INSERT_PASSWORD_FIELD'

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-+=\|?>.<,'
random.seed = (os.urandom(1024))

name = json.loads(open('names.json').read())
domain = json.loads(open("domains.json").read())

#while(1):
#    nameAdd = ''.join(random.choice(name).lower())
#    digitAdd = ''.join(random.choice(numbers) for i in range(0, 4))
#    domainAdd = ''.join(random.choice(domain))
#
#    username = nameAdd + digitAdd + domainAdd
#    password = ''.join(random.choice(chars) for i in range(0, 20))
#
#    requests.post(url, allow_redirects=False, data={
#        usernameField: username
#        passwordField: password
#    })
#
#    print("Sending username %s and password %s" % (username, password))

while(1):
    nameAdd = ''.join(random.choice(name).lower())
    digitAdd = ''.join(random.choice(string.digits) for i in range(0, 4))
    domainAdd = ''.join(random.choice(domain))

    username = nameAdd + digitAdd + domainAdd
    password = ''.join(random.choice(chars) for i in range(0, 20))

    print("Sending username %s and password %s" % (username, password))
