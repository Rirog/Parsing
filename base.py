"""Создание базы данных"""
from peewee import SqliteDatabase, Model, ForeignKeyField, TextField
 
db = SqliteDatabase('sqlite.db') 
 
class DB(Model): 
 
    class Meta: 
        database = db 
 
class Genres_list(DB):
    Genre = TextField()

class Anime_list(DB):
    Anime = TextField()
    Link = TextField()
    Genres = ForeignKeyField(Genres_list)



db.connect()
db.create_tables([Anime_list,Genres_list], safe=True)
db.close()
