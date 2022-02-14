# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import MovieSerializer, DirectorSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def director_list(request):
    director = Director.objects.all()
    data = DirectorSerializer(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"massage": 'F*ck out'})
    data = DirectorSerializer(director).data
    return Response(data=data)

@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"massage": 'F*ck out'})
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"massage": 'F*ck out'})
    data = ReviewSerializer(review).data
    return Response(data=data)


