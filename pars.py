"""Парсинг сайта аниме"""
import requests
import json
from bs4 import BeautifulSoup
from base import Anime_list, Genres_list
#https://animego.org/anime?sort=a.createdAt&direction=desc
def get_anime(url):
    """Запись всех аниме"""
    all_anime_list = {}
    for i in range(1):
        url1 = url + "&page=" + str(i+1)
        req = requests.get(url1)
        scr = req.text
        soup = BeautifulSoup(scr, 'html.parser')
        all_anime_title = soup.find_all(attrs={'class':'h5 font-weight-normal mb-1'})
        all_anime_genres = soup.find_all(attrs={'class':'anime-genre d-none d-sm-inline'})

        for item in all_anime_title:
            item_link = item.find("a").get('href')
            name_anime = item.text
            Anime_list.get_or_create(
                Anime = name_anime,
                Link = item_link
            )
            #all_anime_list[item.text] = f'{item_link}, {item_genres}'
        
        for genre in all_anime_genres:
                item_genres = genre.text
                Genres_list.get_or_create(
                     Genre = item_genres
                )    
                      
            
    #with open('all_anime_list1.json','w',encoding='utf-8') as f:
        #json.dump(all_anime_list, f, indent=4, ensure_ascii=False)

get_anime('https://animego.org/anime?sort=a.createdAt&direction=desc')


