from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Post, Valoracion
from .serializers import PostSerializer, ValoracionSerializer
from rest_framework import permissions

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]