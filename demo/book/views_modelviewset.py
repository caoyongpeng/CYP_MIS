from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from book.serializers import BookSerializers

from book.models import BookInfo

class BooksView(ModelViewSet):
    serializer_class = BookSerializers

    queryset = BookInfo.objects.all()

    @action(methods=['get'], detail=False)  # methods指定匹配的请求方式 detail指定是否在路径生成正则匹配
    def last_book(self, request):
        book = BookInfo.objects.latest('id')
        ser = self.get_serializer(book)
        return Response(ser.data)

    # 根据阅读量获取图书
    @action(methods=['get'], detail=True)
    def bread_book(self, request, pk):
        try:
            book = BookInfo.objects.get(bread=pk)
        except:
            return Response({})

        ser = self.get_serializer(book)

        return Response(ser.data)