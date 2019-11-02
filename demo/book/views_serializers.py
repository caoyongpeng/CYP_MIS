import json

from django.http import JsonResponse
from django.views import View
from book.serializers import BookSerializers,HeroSerializers
from book.models import BookInfo, HeroInfo
from book.modelserializers import HeroModelSerializer

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
        ser = BookSerializers(book,data=data_dict)
        ser.is_valid()
        if ser.errors:
            return JsonResponse({'error':'更新失败'})
        validated_data = ser.validated_data
        ser.save()
        return JsonResponse(ser.data)



    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error':'图书不存在'})
        book.is_delete = True

        return JsonResponse({})

class HeroInfoView(View):
    def get(self,request):
        heros = HeroInfo.objects.all()

        ser = HeroModelSerializer(heros,many=True)

        return JsonResponse(ser.data,safe=False)
    def put(self,request,pk):

        try:
            hero = HeroInfo.objects.get(id=pk)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'error':'不存在'})
        data_dict = json.loads(request.body.decode())

        ser = HeroModelSerializer(hero,data=data_dict)

        ser.is_valid()
        if ser.errors:
            return JsonResponse({'error':'更新失败'})

        ser.save()
        return JsonResponse(ser.data)