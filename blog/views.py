from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    data = Blog.objects.all()
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            form.save()
            form = BlogForm
    context ={"data": data, "form": form}
    return render(request, "index.html", context)
