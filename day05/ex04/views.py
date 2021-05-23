from django.shortcuts import render, HttpResponse
from django.forms import Form
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
        cur.execute('''CREATE TABLE IF NOT EXISTS ex04_movies (
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


def populate(request):
    data = [
        {'episode_nb': 1,
        'title': 'The Phantom Menace',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '1999-05-19'},
        {'episode_nb': 2,
        'title': 'Attack of the Clones',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2002-05-16'},
        {'episode_nb': 3,
        'title': 'Revenge of the Sith',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2005-05-19'},
        {'episode_nb': 4,
        'title': 'A New Hope',
        'director': 'George Lucas',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1977-05-25'},
        {'episode_nb': 5,
        'title': 'The Empire Strikes Back',
        'director': 'Irvin Kershner',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1980-05-17'},
        {'episode_nb': 6,
        'title': 'Return of the Jedi',
        'director': 'Richard Marquand',
        'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
        'release_date': '1983-05-25'},
        {'episode_nb': 7,
        'title': 'The Force Awakens',
        'director': 'J. J. Abrams',
        'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
        'release_date': '2015-12-11'},
    ]
    conn = None
    log_str = ''
    try:
        conn = psycopg2.connect(database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
            )
        cur = conn.cursor()
        for row in data:
            try:
                cur.execute('''INSERT INTO ex04_movies (
                    title, episode_nb, director, producer, release_date)
                    VALUES (%(title)s, %(episode_nb)s, %(director)s,
                    %(producer)s,%(release_date)s)
                    ''', row)
                conn.commit()
                log_str += 'OK<br>'
            except psycopg2.Error as e:
                log_str += 'Error: insert "{}" {}<br>'.format(row['title'], e)
        if cur and not cur.closed:
            cur.close()
    except psycopg2.Error as e:
        print('E: ', e)
        return HttpResponse('Error: {}'.format(e))
    finally:
        if conn and not conn.closed:
            conn.close()
    return HttpResponse(log_str)


def display(request):
    conn = None
    try:
        conn = psycopg2.connect(database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
            )
        cur = conn.cursor()
        cur.execute('''SELECT 
            episode_nb, title, opening_crawl, director,
            producer, release_date
            FROM ex04_movies
            ORDER BY episode_nb
            ''')
        data = cur.fetchall()
        if cur and not cur.closed:
            cur.close()
    except psycopg2.Error as e:
        return HttpResponse('No data available')
    except Exception as e:
        return HttpResponse('No data available')
    finally:
        if conn and not conn.closed:
            conn.close()
    if data:
        return render(request, 'ex04/display.html', {'data' :data})
    else:
        return HttpResponse('No data available')


def remove(request):
    conn = None
    data = None
    form = Form()
    try:
        conn = psycopg2.connect(database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret',
            )
        cur = conn.cursor()
        if request.method == "POST":
            form = Form(request.POST)
            if form.is_valid() and request.POST['select']:
                cur.execute("DELETE FROM ex04_movies WHERE episode_nb = %s;", (request.POST['select'],))
                conn.commit()
        cur.execute('''SELECT 
            episode_nb, title
            FROM ex04_movies
            ORDER BY episode_nb
            ''')
        data = cur.fetchall()
        if cur and not cur.closed:
            cur.close()
    except psycopg2.Error as e:
        return HttpResponse('No data available')
    except Exception as e:
        return HttpResponse('No data available')
    finally:
        if conn and not conn.closed:
            conn.close()
    if data:
        return render(request, 'ex04/remove.html', {'data': data, 'form': form})
    else:
        return HttpResponse('No data available')
