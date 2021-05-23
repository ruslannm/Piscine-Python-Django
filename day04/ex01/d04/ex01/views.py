from django.shortcuts import render


def django(request):
    return render(request, 'content.html',
        {'title' : 'Ex01: Django, framework web.',
         'stylesheet' : 'style1.css',
         'iframe_url': 'https://en.wikipedia.org/wiki/Django_(web_framework)'
        }
        )
    

def display(request):
    return render(request, 'content.html',
        {'title' : 'Ex01: Display process of a static page.',
         'stylesheet' : 'style1.css',
         'iframe_url' : 'https://en.wikipedia.org/wiki/Model–view–controller',
        }
)


def templates(request):
    return render(request, 'content.html',
        {'title' : 'Ex01: Template engine.',
         'stylesheet' : 'style2.css',
         'iframe_url' : 'https://djangobook.com/mdj2-django-templates/',
        }
)
