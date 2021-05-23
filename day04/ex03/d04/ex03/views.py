from django.shortcuts import render
from django.http import HttpResponseRedirect

def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def rows():
    rows = list()
    for i in range(0, 255, 5):
        rows.append((rgb2hex(i, i, i),
            rgb2hex(i, 0, 0),
            rgb2hex(0, 0, i),
            rgb2hex(0, i, 0),
            ))
    return rows


def index(request):
    return render(request, 'index.html',
        {
            'rows' : rows()
        }
        )
