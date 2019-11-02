from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.response import Response

from book.models import BookInfo
from book.serializers import BookSerializers


class BooksView(GenericAPIView,CreateModelMixin,ListModelMixin):
    serializer_class = BookSerializers

    queryset = BookInfo.objects.all()

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class BookView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):

    serializer_class = BookSerializers
    queryset = BookInfo.objects.all()

    def get(self,request,pk):
        return self.retrieve(request)

    def post(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)