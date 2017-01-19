from django.shortcuts import render
from food.forms import ProjectForm
from django.http import HttpResponse
from foodapp.models import Project
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render


# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
    errors = []
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            travel = Project.objects.filter(name__icontains=q)
            return render(request, 'display.html',
                          {'travel': travel, 'query': q})

    full=Project.objects.all()
    return render(request, 'list.html',
                  {'errors': errors,'full':full})

def contact(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            Project.objects.create(name=cd['name'],location=cd['location'],notes=cd['notes'],image=request.FILES['image'])
        form = ProjectForm()
        return render(request,'submit.html',{'form': form})
    else:
        form = ProjectForm()
    return render(request, 'submit.html', {'form': form})



