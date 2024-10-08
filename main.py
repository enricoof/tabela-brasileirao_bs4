# BS é usado em conjunto com as requests
import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)

# Ler o código html:
site = BeautifulSoup(requisicao.text, "html.parser")

tabela = site.find("tbody", class_="score")
times = site.find_all("div", class_="visible-sm")
linhas = tabela.find_all("tr")

teams_list = [time.get_text().strip() for time in times]

points_list = [linha.find("td").get_text().strip() for linha in linhas]

# for team, point in zip(teams_list, points_list):
#     print(f"Time: {team}, Pontos: {int(point)}")

tabelaCsv = pd.DataFrame(list(zip(teams_list, points_list)), columns=['Título', 'Pontos'])
print(tabelaCsv)

tabelaCsv.to_csv('Brasileirão BS4.csv')
