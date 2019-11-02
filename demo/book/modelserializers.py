
from rest_framework import serializers

from book.models import HeroInfo


class HeroModelSerializer(serializers.ModelSerializer):
    # ModelSerializer 和Serializer区别
    # 1、ModelSerializer可以根据指定的模型类自动生成序列化器字段
    # 2、帮助实现了保存和更新方法
    # 3、如果模型类字段指定了唯一，会生成唯一值验证方法

    # 显示指明
    # hbook = serializers.StringRelatedField()
    # hbook_id = serializers.IntegerField()
    # is_delete=serializers.BooleanField(default=False)
    # hname=serializers.CharField(max_length=100,min_length=50)
    #
    # password=serializers.CharField()

    class Meta:
        # 指定根据那个模型类生成序列化字段
        model = HeroInfo
        # 指定字段内容
        fields = '__all__'
        # fields= ('id','hname','hbook','hbook_id','is_delete','password')
        # 取反
        # exclude = ('id',)
        # 给字段增加或修改选项参数
        extra_kwargs = {
            'hname': {
                'min_length': 3,
                'max_length': 30
            }
        }