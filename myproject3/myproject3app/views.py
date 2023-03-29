from django.shortcuts import render


# Create your views here.
def rest(request):
    return render(request, 'index.html')


def viande(request):
    return render(request, 'viande.html')

