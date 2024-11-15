from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def progress_view(request):
    return render(request, "progress.html")
