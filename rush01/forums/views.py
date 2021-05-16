# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# from django.conf import settings
# Create your views here.
 
def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'home.html',context)
 
def addInForum(request):
    if not request.user.is_authenticated:
        return redirect('/')  
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(request.user.name,request.user.email )
            f = forum.objects.create(
                name=str(request.user.username),
                email=request.user.email,
                author=request.user,
                topic=data['topic'],
                description=data['description'],
                )
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)