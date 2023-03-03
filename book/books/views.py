from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/api/v1/get_books/',
        'Detail View': '/api/v1/get_book/<int:pk>/',
        'Create': 'api/v1/create_book/',
        'Update': 'api/v1/update_book/<int:pk>/',
        'Delete': 'api/v1/delete_book/<int:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    queryset = Book.objects.get(id=pk)
    serializer = BookSerializer(queryset)

    return Response(serializer.data)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, pk):
    queryset = Book.objects.get(id=pk)
    queryset.delete()

    return Response(status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
def update_book(request, pk):
    queryset = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
