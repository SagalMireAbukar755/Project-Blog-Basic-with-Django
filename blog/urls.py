from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_view, name="starting_page"),
    path('posts/', views.post_view, name="posts_page"),
    path('posts/<slug:slug>', views.all_view, name="posts-detail-page")
]
