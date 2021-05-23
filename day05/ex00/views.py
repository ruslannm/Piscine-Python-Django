from django.shortcuts import render, HttpResponse
import psycopg2
# Create your views here.

def init(request):
    conn = None
    try:
        conn = psycopg2.connect(database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
            )
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb SERIAL PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
            )
            ''')
        conn.commit()
        if cur and not cur.closed:
            cur.close()
    except psycopg2.Error as e:
        print('E: ', e)
        return HttpResponse('Error: {}'.format(e))
    finally:
        if conn and not conn.closed:
            conn.close()
    return HttpResponse('OK')
    