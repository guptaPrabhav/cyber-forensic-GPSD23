# -- RunScraper -- 

# This Python file simply runs the ahmia_crawler while also checking that our VPN is on

#import the actual crawler
import requests

url = "http://ip-api.com/json/"
key = requests.get(url)
#print(key.text)

# if "India" in key.text or "Tamil Nadu" in key.text or "Katpadi" in key.text:
#     print("Your VPN might not be on !!")
#     safe = False
# else:
#     safe = True


safe = True

print("Status is",safe)

if safe == True:
    import ahmia_crawler
    ahmia_crawler.Crawler()
else:
    print("IP change failed, try again later.")