from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from book.models import BookInfo
from book.serializers import BookSerializers

class BooksView(ListCreateAPIView):
    serializer_class = BookSerializers
    queryset = BookInfo.objects.all()

class BookView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializers
    queryset = BookInfo.objects.all()