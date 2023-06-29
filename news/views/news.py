from rest_framework import viewsets
from ..models.news import News
from ..serializers.news import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
