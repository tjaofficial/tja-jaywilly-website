from django.shortcuts import render
from ..models import videoLinks, socialLinks

def artist_page_view(request, artistName):
    print(artistName)
    videoQuery = videoLinks.objects.all()
    socialQuery = socialLinks.objects.all()
    spotifyURI = False
    for artist in socialQuery:
        if artist.artistName.lower() == artistName:
            spotifyURI = artist.spotifyURI
        
    
    videoList = []
    for video in videoQuery:
        if video.artistName.lower() == artistName:
            videoList.append(video)

    return render(request, 'artist_page_template.html', {
        'header': True,
        'noFooter': True,
        'videoList': videoList,
        'spotifyURI': spotifyURI,
        'artistName': artistName
    })

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