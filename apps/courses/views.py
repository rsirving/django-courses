from django.shortcuts import render, redirect
from django import forms
from .models import Course
from .forms import courseForm

# Create your views here.
def index(request):
    form = courseForm()
    context = {
        "courses": Course.objects.all(),
        "form": form
    }
    return render(request, 'index.html', context)

def new(request):
    if request.method =="POST":
        errors = Course.objects.basic_validator(request.POST)
        form = courseForm(request.POST)
        if errors:
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            course = form.save(commit=False)
            course.save()
            return redirect('/')
    else:
        return redirect('/')

def destroy(request, id):
    if request.method == "POST":
        form = Course.objects.get(id=id)
        form.delete()
        return redirect('/')
    else:
        return redirect('/')