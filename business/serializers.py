from rest_framework import serializers
from .models import Business, Detail, Comment, Type, User, Account, Images
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username',]



class AccountGmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['_id', 'username', 'contact', 'external_pic', ]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["types"]
        
        
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["image2","image3", "image4"]


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = [

            '_id',
            'name',
            'get_image',
            'prix',
            'description',
            'livraison',
            'business_id'
        ]


class CommentsSerializer(serializers.ModelSerializer):
    author = AccountSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Comment
        fields = [

            '_id',
            'body',
            'author'

        ]

class BusinessSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True, required=False)
    liked = AccountSerializer(many=True, read_only=True, required=False)
    carousel = ImagesSerializer(many=False, read_only=True)
    type = TypeSerializer(many=False, read_only=True)
    
    class Meta:
        model = Business
        fields = [
            '_id',
            'name',
            'get_image',
            'contact_tel',
            'description',
            'type',
            'numbers_likes',
            'to_be_visited',
            'comments',
            'liked',
            'carousel'

        ]


