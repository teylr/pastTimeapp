from random import choice
import pandas as pd
import mysql.connector

df = pd.read_sql("jikan_db") #check this i have no fucking clue what im doing

#use jikan for scraping data for anime and then putting it into the database
#pandas - for reading and extracting for the database
#mysql - for the database
#dear pygui - for making the application
#find another api for books
anime = ['naruto', 'onepiece','gintama','bleach','blue lock', 'seraph of the end']
manga = ['boys abyss','berserk','one piece','etc']
choiceOfPastTime = input("What do you want to do? ")

if choiceOfPastTime == 'anime':
    print(choice(anime))
elif choiceOfPastTime == 'manga':
    print(choice(manga))
else:
    print("Sorry, that's not something you can do")

#sample sql connection


# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Homunculus24!",
        database="jikan_db"
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

