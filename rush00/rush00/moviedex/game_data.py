#!/usr/bin/python3
from django.conf import settings
# import settings
from . import  parse_imdb
import random
import pickle

class GameData():
    def __init__(self):
        self.game_file = settings.FT_GAMEFILE
        self.amount_film = settings.FT_AMOUNT_FILM
        self.data = dict()


    def load(self):
        with open(self.game_file, 'rb') as f:
             self.data = pickle.load(f)
        return self

    def dump(self):
        with open(self.game_file, 'wb') as f:
            pickle.dump(self.data, f)


    def get_random_movie(self):
        keys = list(self.data.get('movies').keys())
        if keys:
            return random.choice(keys)
        else:
            return None


    def load_default_settings(self):
        movies = parse_imdb.get_moviemons(self.amount_film)
        self.data = {'player_strength' : 7,
            'player_position' : (0, 0),
            'movies' :movies,
            'movies_caught': dict()
        }
        return self


    def get_strength(self):
        return self.player_strength


    def get_movie(self, moveiID):
        if self.data.get('movies_caught').get(moveiID):
            return {moveiID : self.data.get('movies_caught').get(moveiID)}
        else:
            return None


    def move_to_caught(self, moveiID):
        movie = self.data.get('movies').pop(moveiID, None)
        if movie: 
            self.data.get('movies_caught')[moveiID] = movie


if __name__ == '__main__':
    g = GameData()
#    g.load()
#    g.load_default_settings()
#    print(g.data.get('movies'))
    m_ID = g.get_random_movie()
#    print(m_ID)
    g.move_to_caught(m_ID)
    print(g.get_movie(m_ID))
    print(g.data['player_strength'])
    g.dump()
    g.load()
    print('after dump and load')
    print(g.get_movie(m_ID))
    print(g.data['player_strength'])
