from datetime import timezone

from django.shortcuts import render
from django.views.generic import ListView

def home_page(request):

    return render(request, '_page.html')




