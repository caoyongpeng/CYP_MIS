
from rest_framework.views import APIView
from rest_framework.response import Response
from book.serializers import BookSerializers
from book.modelserializers import HeroModelSerializer
from book.models import BookInfo,HeroInfo



class BooksView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()

        ser = BookSerializers(books,many=True)

        return Response(ser.data)
    def post(self,request):
        data_dict = request.data
        ser = BookSerializers(data=data_dict)
        ser.is_valid()
        if ser.errors:
            return Response({'error':'添加失败'})
        ser.save()
        return Response(ser.data)

class BookView(APIView):
    def get(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'查询失败'})
        ser = BookSerializers(book)
        return Response(ser.data)
    def put(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'没有图书'})
        book_dict = request.data
        ser = BookSerializers(book,data=book_dict)
        ser.is_valid()
        if ser.errors:
            return Response({'error':'添加失败'})
        ser.save()
        return Response(ser.data)
    def delete(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'没有图书'})
        book.is_delete=True
        book.save()
        return Response({})
class HeroView(APIView):
    def get(self,request):
        heros = HeroInfo.objects.all()
        ser = HeroModelSerializer(heros,many=True)
        return Response(ser.data)
    def post(self,request):
        data = request.data

        ser = HeroModelSerializer(data=data)

        ser.is_valid()
        if ser.errors:
            return Response({'error':'添加失败'})
        ser.save()
        return Response(ser.data)