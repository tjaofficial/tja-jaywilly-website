from django.shortcuts import render
from ..models import videoLinks


def tjaofficial_view(request):
    videoQuery = videoLinks.objects.filter(artistName='tjaofficial')
    
    return render(request, 'tjaofficial.html', {
        'header': True,
        'noFooter': True,
        'videoQuery': videoQuery
    })
    
def jaywilly_view(request):
    return render(request, 'jaywilly.html', {
        'header': True
    })