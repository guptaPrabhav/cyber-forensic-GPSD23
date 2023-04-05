#  -- AHMIA SCRAPER --

def Scraper():
    import requests
    import random
    
    yourquery = str(input("Enter space seperated querry string : "))  # such as 'pirated movies', 'gun trade', 'drug traficking', etc

    if " " in yourquery:
        yourquery = yourquery.replace(" ","+")

    url = "https://ahmia.fi/search/?q={}".format(yourquery)
    #print(url)

    #Setting up some fake user agents
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
        "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
        "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
        ]
    
    ua = random.choice(ua_list)     # select a random user agent from the above list
    
    headers = {'User-Agent': ua}

    request = requests.get(url, headers=headers)
    
    content = request.text

    def findlinks(content):
        # Takes in content - webpage in string format - then searches it with regex
        import re
        import random # For generating lists of sites - file name easily
        
        regexquery = "\w+\.onion"   # regex query for finding onion links

        mineddata = re.findall(regexquery, content)

        n = random.randint(1,9999)
        
        filename = "sites{}.txt".format(str(n))     # To avoid overwriting current file
        print("Saving to ... ", filename)
        mineddata = list(dict.fromkeys(mineddata))  # Removing duplicate URLs
        
        with open(filename,"w+") as _:              # Creating a simple text file for storing scraped URLs
            print("")
        for k in mineddata:
            with open(filename,"a") as newfile:
                k  = k + "\n"
                newfile.write(k)
        print("All the files written to a text file : ", filename)



    if request.status_code == 200:
        print("Request went through. \n")
        #print(content)
        findlinks(content)

    # now we COULD use something that reads HTML well
    # like BeautifulSoup - but we could also do something
    # way easier and use RegEx
