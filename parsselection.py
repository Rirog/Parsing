"""Парсинг описания аниме"""
import requests
from bs4 import BeautifulSoup
from base import Test
def all_spisok(url):
    """Получени информации аниме"""
    fullanime = requests.get(url, timeout=10)
    bs = fullanime.text
    soup = BeautifulSoup(bs, 'html.parser')
    selection = soup.find(name='div', attrs={'class':'anime-info'})

    allsal = selection.find_all(attrs={'class':'col-6 col-sm-8 mb-1'}, limit=10)
    allgenre = selection.find(attrs={'class':'col-6 col-sm-8 mb-1 overflow-h'})
    genre = allgenre.text

    text = []
    for al in allsal:
        text.append(al.text)
    types = text[0:1]
    episodes = text[1:2]
    status = text[2:3]
    origin = text[3:4]
    studio = text[6:7]
    agelimit = text[8:9]
    voiceover = text[9:10]
    genre = allgenre.text
    Test.get_or_create(
        Type = types,
        Episodes = episodes,
        Status = status,
        Genre = genre,
        Origin = origin,
        Agelimit = agelimit,
        Studio = studio,
        Voiceover = voiceover,
    )

#print()
url2 = ('https://animego.org/anime/novye-vrata-2583')
all_spisok(url2)
