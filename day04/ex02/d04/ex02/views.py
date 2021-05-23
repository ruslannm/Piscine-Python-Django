from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputText

from datetime import datetime
from django.conf import settings


def get_logs():
    try:
        with open(settings.FT_LOGFILE, 'r') as f:
            logs = f.readlines()
        return logs
    except IOError as e:
        return []


def write_log(post_text):
    if post_text:
        print(post_text)
    date = datetime.now()
    with open(settings.FT_LOGFILE, 'a+') as f:
        f.write("{}  :  {}\n".format(date.strftime("%b %d %Y %H:%M:%S"), post_text))


def index(request):
    form = InputText()
    return render(request, 'index.html', {
        'form': form,
        'logs': get_logs(),
    })


def new_post(request):
    if request.method == 'POST':
        form = InputText(request.POST)
        if form.is_valid():
            print(request.POST)
            write_log(request.POST.get('post_text'))
            return HttpResponseRedirect('/ex02')
