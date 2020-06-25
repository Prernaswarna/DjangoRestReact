from django.urls import path,include
from fixer import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include



router = DefaultRouter()
router.register(r'project' , views.ProjectViewSet)
router.register(r'user' , views.UserViewSet)
router.register(r'bug' , views.BugViewSet)
router.register(r'comment' , views.CommentViewSet)
urlpatterns=[
        path('' , include(router.urls)),
    ]

urlpatterns+=[
        path('api-auth/' , include('rest_framework.urls')),
        ]

