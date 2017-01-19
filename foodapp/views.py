from django.shortcuts import render
from food.forms import ContactForm,ListForm,UserForm
from django.http import HttpResponse
from foodapp.models import Place,List,Country
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
            travel = Place.objects.filter(name__icontains=q)
            return render(request, 'search_results.html',
                          {'travel': travel, 'query': q})

    full=Place.objects.all()
    return render(request, 'search_form.html',
                  {'errors': errors,'full':full})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST ,request.FILES or None )
        if form.is_valid():
            cd = form.cleaned_data
            Place.objects.create(name=cd['name'],location=cd['location'],notes=cd['notes'],image=request.FILES['image'])
        form = ContactForm()
        return render(request,'contact_form.html',{'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})



