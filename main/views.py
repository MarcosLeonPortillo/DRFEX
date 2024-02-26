from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Post, Valoracion
from .serializers import PostSerializer, ValoracionSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
