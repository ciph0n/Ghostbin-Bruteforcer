import requests
import string
import random

possibleCharacters = "0123456789" + string.ascii_lowercase

webhookURL = "#"

r = requests

def codeGenerator():
    codeString = ""
    stringSize = 5
    for x in range(stringSize):
        codeString += random.choice(possibleCharacters)
    return codeString

while True:
    binCode = codeGenerator()
    req = r.get(f'https://ghostbin.co/paste/{binCode}/raw')
    url = f"https://ghostbin.co/paste/{binCode}/raw"
    
    if not "Ghost" in req.text:
        print(req.text)

        Message = {
            "embeds": [
                {
                    "title": "Ghostbin Scraper",
                    "url": f"{url}",
                    "fields": [
                        {
                            "name": "Click the URL for the full paste.",
                            "value": "```" + f"{req.text[:1000]}" + "```",
                            "inline": "false"
                        }
                    ]
                }
            ]
        }
        

        
        r.post(webhookURL, json=Message)
