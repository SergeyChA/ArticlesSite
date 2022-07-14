from rest_framework import generics
from articles.models import Article
from .serializers import ArticlesSerializer
from .permissions import IsAdminOrReadOnly


class ArticlesListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

class ArticlesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAdminOrReadOnly, )





    


