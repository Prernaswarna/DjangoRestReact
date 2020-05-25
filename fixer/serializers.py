from rest_framework import serializers
from fixer.models import User , Project , Bug , Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id' , 'username' , 'email' , 'typeofuser']


class ProjectSerializer(serializers.ModelSerializer):
    issues=serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields=['id', 'project_name' , 'wiki' , 'project_members','issues']


class BugSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Bug
        fields=['id','heading' , 'description' , 'doc' , 'tags' , 'status' , 'reporter' , 'project' , 'assignee','comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id' , 'bug' , 'creator' , 'body' , 'created_on']


