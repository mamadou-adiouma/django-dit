from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('article/', views.article, name="article"),
    path('article-detail<int:pk>/', views.article_detail, name="article-detail"),
    path('blog/', views.blog, name="blog"),
    path('404-page/', views.error404, name="404-page")
]