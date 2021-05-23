from django.shortcuts import render, HttpResponse
from .models import Movies

# import psycopg2
# Create your views here.

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
    log_str = ''
    for row in data:
        try:
            new_row = Movies(**row)
            new_row.save()
            log_str += 'OK<br>'
        except Exception as e:
            log_str += 'Error: insert "{}" {}<br>'.format(row['title'], e)
    return HttpResponse(log_str)



def display(request):
    response = None
    try:
        response = Movies.objects.all().order_by('episode_nb')
    except Exception as e:
        return HttpResponse('No data available')
    if response:
        return render(request, 'ex03/display.html', {'data' :response})
    else:
        return HttpResponse('No data available')
