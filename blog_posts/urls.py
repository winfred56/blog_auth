from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create/', views.create, name='create'),
    path('posts/<int:id>/', views.detail, name='detail'),
    path('posts/update/<int:id>/', views.update, name='update'),
    path('posts/delete/<int:id>/', views.delete, name='delete'),
    #path('posts/comment/<int:id>/', views.comments, name='comment'),
    path('posts/comment/<int:id>/update/', views.update_comment, name='update_comment'),
    path('posts/comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
]
