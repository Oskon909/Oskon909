from django.urls import path

from .views import CategoryApi, PostApiView

urlpatterns = [
    path('post/', PostApiView.as_view(), name='post'),
    path('category/',  CategoryApi.as_view(), name='category'),

]