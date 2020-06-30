from rest_framework import serializers
from fixer.models import User , Project , Bug , Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id' , 'username' , 'email' , 'typeofuser','enroll']


class ProjectSerializer(serializers.ModelSerializer):
    issues=serializers.StringRelatedField(many=True, required=False , allow_null=True)
    class Meta:
        model = Project
        fields='__all__'
        read_only_field = ('issues')        


class BugSerializer(serializers.ModelSerializer):
    #comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Bug
        fields='__all__'
        #read_only_fields = ( 'doc', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id' , 'bug' , 'creator' , 'body' , 'created_on']


