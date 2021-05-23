from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import game_data


def get_movies(game):
    keys = list(game.data.get('movies_caught').keys())
    movies = list()
    for key in keys:
        d = game.data['movies_caught'][key]
        movies.append((key, d['name'], 
                d['poster'], d['director'], d['year'], d['rating'], d['synopsis'], d['actors']))
    return movies                


def index(request):
    g = game_data.GameData()
    g = g.load_default_settings()


    m_ID = g.get_random_movie()
    g.move_to_caught(m_ID)
    m_ID = g.get_random_movie()
    g.move_to_caught(m_ID)
    return render(request, 'index.html',
    {'movies' : g.data['movies_caught'],}, )