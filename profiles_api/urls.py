from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset,base_name='hello-viewset')

urlpatterns = [
    path('myfirst-apiview/',views.HelloApiView.as_view()),
    path('',include(router.urls)),
]
