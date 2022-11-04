from dataclasses import fields
from rest_framework import serializers
from .models import Artiste, Song, Lyric

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('__all__')
        
class ArtisteSerializer(serializers.ModelSerializer):
    Songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artiste
        fields = ('first_name', 'last_name', 'age', 'Songs')
        