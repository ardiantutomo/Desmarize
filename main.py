from desmarize import Scrapper
from desmarize import Summarizer

def main():
    query = input("What do you want to search: ")
    oxford = Summarizer.summarize(Scrapper.getOxford(query))
    wikipedia = Summarizer.summarize(Scrapper.getWikipedia(query))
    description = "".join(oxford) + " " + "".join(wikipedia)

    print (description)

main()