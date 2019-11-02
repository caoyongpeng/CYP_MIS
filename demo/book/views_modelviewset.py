from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from book.serializers import BookSerializers

from book.models import BookInfo

class BooksView(ModelViewSet):
    serializer_class = BookSerializers

    queryset = BookInfo.objects.all()