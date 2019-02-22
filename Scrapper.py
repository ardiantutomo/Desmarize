import requests
from bs4 import BeautifulSoup
import re

def getOxford(title):
    #https://en.oxforddictionaries.com/definition/
    try:        
        url = "https://en.oxforddictionaries.com/definition/" + title    
        r = requests.get(url)

        # print (request.content)

        soup = BeautifulSoup(r.content, 'html.parser')
        definition = soup.find("span", {"class":"ind"})
        return (definition.text)
    except:
        return ""

def getWikipedia(title):
    try:
        url = "https://en.wikipedia.org/wiki/" + title    
        r = requests.get(url)

        # print (request.content)

        soup = BeautifulSoup(r.content, 'html.parser')
        definition = soup.find_all("p")
        result = [j.text for j in definition] #get all text in wikipedia
        result = [j.rstrip() for j in result if j != "\n"] #delete \n in list
        return ("".join(result))
    except:
        return ""

def getDescription(title):
    return ''.join(getOxford(title)) + " " + ''.join(getWikipedia(title))
