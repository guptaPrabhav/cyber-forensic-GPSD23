# -- TOR Searcher -- 

# Searching the Tor network for the urls found on 'ahmia.fi'

# The code defines a Python script that uses the Tor network to make anonymous HTTP requests to a list of URLs provided in a newline-separated text file and saves the HTML response of each URL to individual text files. It utilizes the `requests` library and a Tor proxy to achieve this functionality.

def torSearcher(url):
    # BEFORE YOU START - RUN tor.exe !!!!
    
    import requests
    import random
    def get_tor_session():
        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {
                           'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'
                          }
        return session

    # Make a request through the Tor connection
    # IP visible through Tor
    session = get_tor_session()
    #url = "http://httpbin.org/ip"
    #url = "http://x.onion/"

    print("Getting ...", url)
    result = session.get(url).text
    # Above should print an IP different than your public IP
    # Following prints your normal public IP
    #print(requests.get("http://httpbin.org/ip").text)

    # url = "http://x.onion/"
    # url = url.replace("http://","")
    # url = url.replace(".onion","")
    # url = url.replace("/","")
    # or  u can use the name
    
    import string
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    with open(f"{filename}.txt","w+", encoding="utf-8") as newthing:
        newthing.write(result)

# url = "http://x.onion"
# torSearcher(url)

import sys
import os
programname = os.path.basename(sys.argv[0])

print(sys.argv)


# path = '/home/Maltego_Hackathon'
# entries = os.listdir(os.path.basename(path))
# print(path)

try:
    thelist = sys.argv[1]
    print(thelist)
    print("Opening ...", thelist)
    with open(thelist, "r", encoding="utf-8") as newfile:
        data = newfile.readlines()
        try:
            #
            for k in data:
                k = k.replace("\n","")
                k = "http://" + k
                torSearcher(k)
        except Exception as E:
            print(E)
except:
    print("Usage : {} <newlineSeperatedList.txt>".format(programname))
    
    
