from rest_framework import viewsets, filters, pagination, status
from .models import User
from .serializers import UserSerializers

from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class PageSet(pagination.PageNumberPagination):
    # 每页显示多少个
    page_size = 3
    # 默认每页显示3个
    page_size_query_param = "size"
    # 最大页数
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


class LimitSet(pagination.LimitOffsetPagination):
    # 每页默认几条
    default_limit = 3
    # 设置传入页码数参数名
    page_query_param = "page"
    # 设置传入条数参数名
    limit_query_param = 'limit'
    # 设置传入位置参数名
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = None


class UserViewSet(viewsets.ModelViewSet):

    # 指定结果集并设置排序
    queryset = User.objects.all().order_by('-id')
    # 指定序列化的类
    serializer_class = UserSerializers
    # 指定分页配置
    pagination_class = LimitSet

    # http://127.0.0.1:8000/api/user/?search=sunnan
    # 配置搜索功能
    filter_backends = (filters.SearchFilter,)
    # 设置搜索的关键字
    search_fields = ('=username', 'id')
    # 设置需要被排序的字段
    ordering_fields = ('username', 'id')


def login(request):
    print("登陆方法: "+request.method)
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.get(username=username, password=password).count()
    if user.is_valid():
        ret = {'code': '01', 'msg': '登陆成功', 'result': user}
    else:
        ret = {'code': '02', 'msg': '登陆失败', 'result': user}
    return JsonResponse(ret)

