from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.read_post, name='detail'),
    path('post/create/', views.create_post, name='createPost'),
    path('post/update/<int:post_id>/', views.update_post, name='updatePost'),
    path('post/delete/<int:post_id>/', views.delete_post, name='deletePost'),
]