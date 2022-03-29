import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate #for nice formatting

#get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_Electronic_Arts_games:_1983%E2%80%931999"
table_class="wikitable sortable jquery-tablesorter" #put whatever class your table is here
response=requests.get(wikiurl)
print(response.status_code) #if it prints 200, it's okay to go ahead and webscrape

#parse from html into object
soup = BeautifulSoup(response.text, 'html.parser')
yourtable=soup.find_all("table",{"class": "wikitable sortable"})

df=pd.read_html(str(yourtable))
#list to df
df=pd.DataFrame(df[0])
print(df)

#drop whatever columns you don't need
data = df.drop(["Release date", "Platforms", "Developer(s)", "Ref(s)"], axis=1)

#if you want to drop duplicates in every column
data = data.drop_duplicates()

with pd.option_context('display.max_rows', None, 'display.max_columns', None): #to show all rows in Google Colab
    print(tabulate(data, showindex=False)) #prints whatever you scraped