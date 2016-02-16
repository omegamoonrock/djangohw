from django.shortcuts import render
from homepage.models import blog
from .forms import BlogPosts


# Create your views here.
def home(request):
    all_objects = blog.objects.all()
    print all_objects

    template="home.html"
    form = BlogPosts(request.POST or None)
    if form.is_valid():
        variable = form.save(commit = False)
        variable.save()

    context={
        "formvar": form,
        "variable1": all_objects,

    }
    return render(request, template, context)