from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Post, Valoracion
from .serializers import PostSerializer, ValoracionSerializer
from rest_framework import permissions
from .permissions import PostPermission

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]



class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]