# from django.shortcuts import render  # => html 이 없어서 필요가 없어진다. 

# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Artist, Music
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer

from IPython import embed

# import json


# 달라  써라     수정    삭제
# Read  Create  Update  Delete
# GET   POST    PATCH   DELETE  


@api_view(['GET'])  # GET 요청에 대해서만 처리한다. 
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)

    return Response(serializer.data)  # 개발자들이 사용하도록 만든 


    # artists = Artist.objects.all()
    # dataset = []
    # for artist in artists:
    #     d = {
    #         "id": artist.id,
    #         "name": artist.name
    #     }
    #     dataset.append(d)

    # # 공용어 == string 으로 바꾸다. (Serialization: 직렬화)
    # res_data = json.dumps(dataset)  # 스트링으로 만들어주는 공용어 과정 
    # print(type(res_data), res_data)

    # return HttpResponse(res_data)

@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = MusicDetailSerializer(music)
    return Response(ser.data)


@api_view(['POST'])
def create_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = CommentSerializer(data=request.data)  # request.POST vs request.data
    if ser.is_valid(raise_exception=True):
        ser.save(music_id=music.id)
    return Response(ser.data)

    



