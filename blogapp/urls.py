from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view(), name="search"),
    path('delete_comment/<int:pk>/', views.delete_comment, name="remove-comment"),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name="update-comment"),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name="update-post"),
    path('create_post/', views.PostCreate.as_view(), name="create-post"),
    path('tag/<str:slug>/', views.tag_page, name="tag"),
    path('category/<str:slug>/', views.category_page, name="category"),
    path('<int:pk>/new_comment/', views.new_comment, name="new-comment"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post-detail"),
    path('', views.PostList.as_view(), name="post-list"),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]