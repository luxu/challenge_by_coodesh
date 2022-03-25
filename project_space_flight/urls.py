from django.contrib import admin
from django.urls import path, include

from api import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'articles', views.ArticlesViewSet, basename='Articles')

urlpatterns = [
    path('', views.index, name="index"),
    path('', include(router.urls)),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('article_details/<int:key>/', views.article_key, name="article_details"),
    path('article/', views.article_new, name="article_new"),
    path('article/<int:key>/', views.article_update, name="article_update"),
    path('article_delete/<int:key>/', views.article_delete, name="article_delete"),
]
