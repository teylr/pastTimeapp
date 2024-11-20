from random import choice
import pandas as pd


#use jikan for scraping data for anime
#find another api for scraping manga
anime = ['naruto', 'onepiece','gintama','bleach','blue lock', 'seraph of the end']
manga = ['boys abyss','berserk','one piece','etc']
choiceOfPastTime = input("What do you want to do? ")

if choiceOfPastTime == 'anime':
    print(choice(anime))
elif choiceOfPastTime == 'manga':
    print(choice(manga))
else:
    print("Sorry, that's not something you can do")