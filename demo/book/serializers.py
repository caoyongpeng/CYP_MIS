from rest_framework import serializers

from book.models import BookInfo

# class HeroSerializers(serializers.Serializer):
#     hname = serializers.CharField(max_length=10)
#     hgender = serializers.IntegerField(read_only=True)
#     hcomment = serializers.CharField()



class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20,min_length=4)
    bpub_date = serializers.DateField(write_only=True,required=False)
    bread = serializers.IntegerField(default=0)
    bcomment = serializers.IntegerField(default=0)
    # heros = HeroSerializers(read_only=True,many=True)
    # heros = serializers.StringRelatedField()

    def validate_btitle(self,value):

        if value == 'python':
            raise serializers.ValidationError('书名错误')

        return value

    def validate(self, attrs):

        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError('阅读量大于评论量')

        return attrs

    def create(self, validated_data):

        book = BookInfo.objects.create(**validated_data)

        return book

class HeroSerializers(serializers.Serializer):
    hname = serializers.CharField(max_length=10)
    hgender = serializers.IntegerField(read_only=True)
    hcomment = serializers.CharField()
    hbook = BookSerializers()