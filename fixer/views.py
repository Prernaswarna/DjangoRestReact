from django.shortcuts import render
from rest_framework.decorators import action , api_view , renderer_classes,permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from fixer.models import Project , User , Bug,Comment
from fixer.serializers import ProjectSerializer , UserSerializer,BugSerializer,CommentSerializer
from django.http import HttpResponse
from rest_framework import permissions , status
from fixer.permissions import IsTeamOrReadOnly , IsAdminOrNoAccess
import requests
import json
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer , TemplateHTMLRenderer
from django.contrib.auth import authenticate , login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
# Create your views here.




class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]
    

    @action(detail=False , methods=['get','post','options',])
    def confirm(self , request ):
        authorization_code = self.request.query_params.get('code')
        print(authorization_code)
        payload = {'client_id':'Z0D8JmQtXjXJxp63bsnt2HEGvWuw7sSRD19oZ4FO' ,'client_secret':'hTgORjftOyZ0zikE5icUEUw22Q1RP3W3tRckzmZsIjBe2W9HegNsU71X9Ps1H8E6N6ZRu4cFhZqUnPf9MKAT8d5Kar9Drp8apcfNHyumFoR38n3JNSPahVmjv1cSmcGw','grant_type':'authorization_code' , 'redirect_url':'http://127.0.0.1:3000/' , 'code' : authorization_code}
        userdata = requests.post('https://internet.channeli.in/open_auth/token/' , data=payload).json()
        acstoken=userdata['access_token']
        print(acstoken)
        headers={'Authorization':'Bearer ' + acstoken}
        userdata = requests.get('https://internet.channeli.in/open_auth/get_user_data/' , headers=headers).json()
        try:
            user=User.objects.get(enroll=userdata["student"]["enrolmentNumber"])
            login(request , user)
            print(user)
            
        except User.DoesNotExist:
            img=False
            for role in userdata["person"]["roles"]:
                if role["role"] == "Maintainer":
                    img=True
                    break
            if img:
                enroll = userdata["student"]["enrolmentNumber"]
                email=userdata["contactInformation"]["emailAddress"]
                name=(userdata["person"]["fullName"]).split()
                username = name[0]+name[1]
                print(userdata["student"]["currentYear"])
                if userdata["student"]["currentYear"]>=3:
                    typeofuser = True
                else :
                    typeofuser = False
                newuser = User(username=username , email=email , typeofuser=typeofuser , enroll=enroll , acstoken = acstoken)
                newuser.is_staff=True
                newuser.save()
                login(request , newuser) 
                return Response({'data':'User Created', 'typeofuser':newuser.typeofuser , 'userId' : newuser.id},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'data':'User not in IMG'},status=status.HTTP_401_UNAUTHORIZED)
        return Response({'data':'User exists', 'typeofuser':user.typeofuser , 'userId':user.id})

    @action(detail=False , methods=['get',])
    def currentuser(self , request ):
        return Response({'userId':self.request.user.id , 'typeofuser':self.request.user.typeofuser})


class BugViewSet(viewsets.ModelViewSet):
    queryset= Bug.objects.all()
    serializer_class=BugSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CommentViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





