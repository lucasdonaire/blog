from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index.as_view(), name='index'),
    path('post/<int:post_id>/', views.read_post.as_view(), name='detail'),
    path('post/create/', views.create_post.as_view(), name='createPost'),
    path('post/<int:post_id>/comment/', views.create_comment, name='createComment'),
    path('post/update/<int:post_id>/', views.update_post.as_view(), name='updatePost'),
    path('post/delete/<int:post_id>/', views.delete_post.as_view(), name='deletePost'),
    path('categorys/', views.categoryListView.as_view(), name='categorys'),
    path('categorys/<int:pk>/', views.categoryDetailView.as_view(), name='detail-category'),
    path('categorys/create', views.categoryCreateView.as_view(), name='create-category'),
]