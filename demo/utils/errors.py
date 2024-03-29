from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from django.db import DatabaseError

def custom_exception_handler(exc,context):

    response = exception_handler(exc,context)

    if response is None:
        view = context['view']
        if isinstance(exc,DatabaseError):
            print('[%s]:%s'%(view,exc))
            response = Response({'detail':'服务器内部错误'},status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response