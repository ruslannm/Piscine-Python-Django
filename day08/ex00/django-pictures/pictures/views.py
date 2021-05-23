from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import PictureModel
from .forms import PictureForm

# Create your views here.
class HomeView(ListView):
    model = PictureModel
    template_name = 'pictures/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = PictureForm
        return context

    def post(self, request , *args , **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class ImageFormViev(FormView):
    template_name = 'pictures/home.html'

    form_class = PictureForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ImageFormViev, self).form_valid(form)
        