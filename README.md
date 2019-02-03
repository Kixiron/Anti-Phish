# Anti-Phish

An anti-phishing script

## **Disclaimer**

**The usage of this script in a criminal manner is not endorsed by me, and you hold all responsibility for your actions.**  
**Never use this script on a website which you do not own.**

## Usage

antiphish.py takes four command-line parameters:

```txt
url
```

The url is a positional argument that should be the target url/domain.

```txt
-p
--password
```

The password is the password field of the request, and will be fed with random strings that look roughly like this `gQbrRih6q#dK-dU=CHMN`.

```txt
-u
--username
```

The username is the username field of the request, and will be fed with random strings that look roughly like this `doug4813@inbox.com`.  
The username field draws from names.json, which contains over 8000 names.

```txt
-dl [True/False]
--domainlist [True/False]
```

The domainlist is a switch that chooses between two domainlists, domains.json (Containing the seven most popular domains), and alldomains.json (Containing every domain I could find).  
`True` = all domains, `False` = common domains

-----

Example usage:

```txt
py antiphish.py website.com/login.php --username usernamefield --password passwordfield --domainlist True
```

-----

## License

Copyright 2019 Kixiron

Licensed under the Apache License, Version 2.0 (the "License");  
you may not use this file except in compliance with the License.  
You may obtain a copy of the License at  

```txt
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and  
limitations under the License.  
