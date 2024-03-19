from django.shortcuts import render, redirect
from ..models import shows
from ..forms import shows_form

def add_shows_view(request):
    showsQuery = shows.objects.all()
    form = shows_form
    
    if request.method == "POST":
        requestCopy = request.POST.copy()
        requestCopy['local'] = True
        formData = shows_form(requestCopy)
        print(formData.errors)
        if formData.is_valid():
            formData.save()
            return redirect('tourDates')
    return render(request, 'add_shows.html', {
        'header': True,
        'form': form
    })