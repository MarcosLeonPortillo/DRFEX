from rest_framework import serializers
from .models import Post, Valoracion, User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['titulo', 'cuerpo', 'user', 'url']


class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Valoracion
        fields = ['rating', 'fecha_registro', 'comment', 'url', 'post', 'user']
