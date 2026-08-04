from django.shortcuts import render, HttpResponse
from .models import CivicLink
# Create your views here.
def home(request):
    return render(request, 'home.html')

def CivicLink(request):
    civic_links = CivicLink.objects.all()
    return render(request, "civiclink.html", {"civic_links": civic_links}) 