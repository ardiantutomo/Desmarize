import requests
from bs4 import BeautifulSoup
import re

def getOxford(title):
    try:        
        url = "https://en.oxforddictionaries.com/definition/" + title    
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        definition = soup.find("span", {"class":"ind"})
        return (definition.text)
    except:
        return ""

def getWikipedia(title):
    try:
        url = "https://en.wikipedia.org/wiki/" + title    
        r = requests.get(url)


        soup = BeautifulSoup(r.content, 'html.parser')
        definition = soup.find_all("p")
        result = [j.text for j in definition] #get all text in wikipedia
        result = [j.rstrip() for j in result if j != "\n"] #delete \n in list
        result = [j.lstrip() for j in result] #delete \n in list
        result = "".join(result)
        if(result=="Other reasons this message may be displayed:"):
            return ""
        return ("".join(result))
    except:
        return ""
