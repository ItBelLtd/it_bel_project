from django.shortcuts import render
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        data = {'title': 'Hello, World!'}
        return render(request, "index.html", data)
