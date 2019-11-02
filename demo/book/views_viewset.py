from rest_framework.viewsets import ViewSet
from book.models import BookInfo
from rest_framework.response import Response
from book.serializers import BookSerializers




class BooksView(ViewSet):
    def list(self,request):
        books = BookInfo.objects.all()

        ser = BookSerializers(books,many=True)

        return Response({'books':ser.data})
    def create(self,request):
        data = request.data
        ser = BookSerializers(data=data)

        ser.is_valid()
        if ser.errors:
            return Response({'errors':ser.errors})
        ser.save()
        return Response(ser.data)
    def retrieve(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'图书不存在'})

        ser = BookSerializers(book)
        return Response({'book':ser.data})
    def update(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'图书不存在'})
        data = request.data
        ser = BookSerializers(book,data=data)
        ser.is_valid()
        if ser.errors:
            return Response({'errors':'更新失败'})
        ser.save()
        return Response(ser.data)

    def destroy(self,request,pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error':'不存在'})

        book.is_delete=True
        book.save()
        return Response({})