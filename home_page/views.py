from datetime import timezone

from django.shortcuts import render

from django.views import View

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'home_page/home.html'
        )




