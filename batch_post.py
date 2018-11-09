import os
import time
import random
import sys
from fake_useragent import UserAgent
from json import load
import urllib.request
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

#specifies useragent, this sort of precaution is necessary if you wish to bot continously
ua = UserAgent()
ua.chrome

#sets proxy via user input
proxyyn = input("Using a proxy? y / n ")
if proxyyn == "n":
    print("No proxy being applied.")
else:
    print("Copy and paste your proxy in the following format:")
    proxy = input("address:port (Requires IP verification through your proxy provider. Just press enter to continue without a proxy.) ")
    print(proxy)
    os.environ['http_proxy'] = proxy 
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    #double checking your proxy is in place
    #safety precaution as accidentally using the wrong ip once on insta could get you banned
    print("Your current IP is:")
    htmlfile = urllib.request.urlopen("http://v6.ipv6-test.com/api/myip.php")
    htmltext = htmlfile.read()
    ip = "colored.clickselect".encode()
    print(htmltext)
    ip_confirm = input("Double check it . Continue with this? y / n ")
    if ip_confirm != "y":
        input("Change your proxy then.")
        sys.exit()
    else:
        print("Continuing")


#instagram username and password specified via user input
username = input("Enter username: ")
print("You entered: " + username)
password = input("Enter password: ")
print("You entered: " + username)

#begins to read from this scripts directory and a specified folder
root = os.getcwd()
post_from = os.getcwd() + "\\placeimagesinhere\\"
print(post_from)
for root, dirs, files in os.walk(post_from):
    for filename in files:
        print(filename)
        print("instapy -u \"" + username + "\" -p \"" + password + "\" -f \"" + post_from + filename + "\" -t test")
        os.system("instapy -u \"" + username + "\" -p \"" + password + "\" -f \"" + post_from + filename + "\" -t \"test")
        #following line waits for specified range of time
        #default is between 10,800 seconds (3 hours) and 18,000 seconds (5 hours)
        os.remove(post_from + filename)
        print("Image was posted. Now waiting for 3 - 5 hrs")
        time.sleep(random.randint(10800,18000))

input("You're out of images! Press enter to exit.")
