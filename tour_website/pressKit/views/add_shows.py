from django.shortcuts import render
from ..models import shows
from ..forms import shows_form

def add_shows_view(request):
    showsQuery = shows.objects.all()
    form = shows_form
    
    if request.method == "POST":
        formData = shows_form(request.POST)
        if formData.is_valid():
            formData.save()
    return render(request, 'add_shows.html', {
        'header': True,
        'form': form
    })