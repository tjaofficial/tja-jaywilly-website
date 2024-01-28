from django.shortcuts import render
from ..models import shows

def tour_dates_view(request):
    showQuery = shows.objects.all().order_by('date')
    return render(request, 'tour_dates.html', {
        'header': True,
        'showQuery': showQuery
    })