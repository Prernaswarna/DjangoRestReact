from django.shortcuts import render
from rest_framework.decorators import action , api_view , renderer_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets
from fixer.models import Project , User , Bug
from fixer.serializers import ProjectSerializer , UserSerializer,BugSerializer
from django.http import HttpResponse
from rest_framework import permissions
from fixer.permissions import IsTeamOrReadOnly , IsAdminOrNoAccess
import requests
import json
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer , TemplateHTMLRenderer
# Create your views here.




class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsTeamOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    @action(detail=True , methods=['get'])
    def first(self , request , pk=None):
        return render(request , 'fixer/index.html')

    @action(detail=False , methods=['post'])
    def confirm(self , request ):
        authorization_code = request.POST.get('code')
        payload = {'client_id':'k9IXT2RD811seHEj8858BIo24rVCCDHsY50ucEj9' ,'client_secret':'Z3HW3CS9A0NH0pGHQshdh17bjsvpOeUO58PmTXmtzh1Tng7BXCgNX2EvZdQs4DX3WkDTswtMjqmnbi10RrvREuC7H8aijB7AsIbpsfiesn7ztOZZ1UqqnooUMg0T6XN2','grant_type':'authorization_code' , 'redirect_url':'127.0.0.8000/homescreen' , 'code' : authorization_code}
        r = requests.post('https://internet.channeli.in/oauth/token/' , params=payload)
        return Response(r.json());
    
    @action(detail=False , methods=['post'])
    def homescreen(self , request):
        access_token=request.POST.get('access_token');
        payload={'access_token':access_token}
        r=requests.post('https://internet.channeli.in/oauth/token/' , params=access_toke);
        return Response(r.json());



class BugViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Bug.objects.all()
    serializer_class=BugSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]









def projectdetails(request , project_id):
    return HttpResponse("This page displays all the details of question %s" %project_id)

def issue(request , project_id):
    return HttpResponse("this page displays all issues related to project id %s" %project_id)


