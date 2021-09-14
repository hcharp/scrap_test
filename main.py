import pandas as pd
import requests
from bs4 import BeautifulSoup
# from settings import (créer variables)
#TODO: variables dans settings.py


url = "https://www.pagesblanches.be/chercher/personne"
noms = ["arnaud", "neyton", "machin"]
results = pd.DataFrame()


#####################################
# code from Stackoverflow (chitown88)
#####################################

# for nom in noms:
#     page = requests.get("{}/{}".format(url, nom))
#     soup = BeautifulSoup(page.content, 'html.parser')

#     lehigh = requests.get(url).text
#     soup = BeautifulSoup(lehigh,'lxml')

#     rows = soup.find_all('div',class_="sidearm-schedule-game-row flex flex-wrap flex-align-center row")

#     sheet = pd.DataFrame()
#     for row in rows:
#         date = row.find('div',class_="sidearm-schedule-game-opponent-date").text.strip()
#         name = row.find('div',class_="sidearm-schedule-game-opponent-name").text.strip()
#         opp = row.find('div',class_="sidearm-schedule-game-opponent-text").text.strip()
#         conf = row.find('div',class_="sidearm-schedule-game-conference-conference").text.strip()

#         try:
#             result = row.find('div',class_="sidearm-schedule-game-result").text.strip()
#         except:
#             result = ''

#         df = pd.DataFrame([[year,date,name,opp,conf,result]], columns=['year','date','opponent','list','conference','result'])
#         sheet = sheet.append(df,sort=True).reset_index(drop=True)

#     results = results.append(sheet, sort=True).reset_index(drop=True)


# results['result'], results['score'] = results['result'].str.split(',', 1).str
# results.to_excel('lehigh.xlsx')