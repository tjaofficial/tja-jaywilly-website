from django.shortcuts import render

def tjaofficial_view(request):
    return render(request, 'tjaofficial.html', {
        'header': True,
        'noFooter': True
    })
    
def jaywilly_view(request):
    return render(request, 'jaywilly.html', {
        'header': True
    })