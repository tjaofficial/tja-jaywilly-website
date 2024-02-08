from django.shortcuts import render
from ..models import shows

def tour_dates_view(request):
    showQuery = shows.objects.all().order_by('date')
    return render(request, 'tour_dates.html', {
        'header': True,
        'showQuery': showQuery
    })
    
def view_shows_view(request, showName):
    showQuery = shows.objects.all().order_by('date')
    return render(request, 'view_shows.html', {
        'header': True,
        'showQuery': showQuery
    })