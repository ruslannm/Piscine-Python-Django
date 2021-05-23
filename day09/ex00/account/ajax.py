from django.http import Http404, HttpResponse
import json
from django.contrib.auth.models import User
from django.contrib import auth


def get_element(request):
    data_in = request.POST
    if request.is_ajax() == True:
        data = json.dumps({
            'user': None
        })
        u = User.objects.filter(username=data_in['username'])
        if u:
            user = auth.authenticate(username=data_in['username'], password=data_in['password'])
            if user and user.is_active:
                auth.login(request, user)
                data = json.dumps({
                    'user': user.get_username()
                })
        return HttpResponse(data, content_type='application/json')
    else:
        data = json.dumps({
            'user': None
        })
    return HttpResponse(data, content_type='application/json')
        