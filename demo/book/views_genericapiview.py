from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from book.modelserializers import HeroModelSerializer
from book.serializers import BookSerializers
from book.models import BookInfo,HeroInfo
from django_filters.rest_framework import DjangoFilterBackend

class BooksView(GenericAPIView):
    serializer_class = BookSerializers

    queryset = BookInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('btitle', 'bread')
    def get(self,request):
        books = self.get_queryset()
        ser = self.get_serializer(books,many=True)
        return Response(ser.data)



    def post(self,request):
        data = request.data
        ser = self.get_serializer(data=data)
        ser.is_valid()
        if ser.errors:
            return Response({'errors': ser.errors})
        ser.save()
        return Response(ser.data)
class BookView(GenericAPIView):

    serializer_class = BookSerializers

    queryset = BookInfo.objects.all()

    def get(self, request, pk):

        book=self.get_object()

        ser = self.get_serializer(book)

        return Response({'books': ser.data})

    def put(self, request, pk):

        book = self.get_object()

        data=request.data

        ser = self.get_serializer(book,data=data)

        try:
            ser.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'errors': e.detail})

        ser.save()

        return Response(ser.data)

    def delete(self, request, pk):

        book=self.get_object()

        book.is_delete = True
        book.save()
        return Response({})