import json

from django.http import JsonResponse
from django.views import View
from book.serializers import BookSerializers
from book.models import BookInfo


class BooksView(View):
    """
        获取所有图书和保存图书
    """

    def get(self, request):
        # 1、查询图书表获取取所有图书信息
        books = BookInfo.objects.all()
        # 2、返回图书信息
        ser = BookSerializers(books,many=True)
        return JsonResponse(ser.data,safe=False)

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict=json.loads(data)
        # 2、验证数据
        ser = BookSerializers(data=data_dict)
        ser.is_valid()
        if ser.errors:
            return JsonResponse({'error':ser.errors})
        vaildated_data = ser.validated_data

        ser.save()
        return JsonResponse(ser.data)


class BookView(View):
    """
        获取单一图书
        更新
        删除
    """

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error':'图书不存在'})
        return JsonResponse({'id': book.id,
                            'btitle': book.btitle,
                            'bread': book.bread,
                            'bpub_date': book.bpub_date,
                            'bcomment': book.bcomment,})

    def put(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error':'图书不存在'})
        data_dict = json.loads(request.body.decode())
        res = BookInfo.objects.filter(id=pk).update(**data_dict)
        if res == 0:
            return JsonResponse({'error':'更新失败'})
        book = BookInfo.objects.get(id=pk)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bread': book.bread,
            'bpub_date': book.bpub_date,
            'bcomment': book.bcomment,
        })


    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error':'图书不存在'})
        book.is_delete = True

        return JsonResponse({})