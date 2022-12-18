from django.urls import path
from . import views

app_name = "blogquestionapp"

urlpatterns = [
    path('search/<str:q>/', views.QuestionPostSearch.as_view(), name="search"),
    path('delete_comment/<int:pk>/', views.delete_comment, name="remove-comment"),
    path('update_comment/<int:pk>/', views.QuestionCommentUpdate.as_view(), name="update-comment"),
    path('update_post/<int:pk>/', views.QuestionPostUpdate.as_view(), name="update-post"),
    path('create_post/', views.QuestionPostCreate.as_view(), name="create-post"),
    path('tag/<str:slug>/', views.tag_page, name="tag"),
    path('category/<str:slug>/', views.category_page, name="category"),
    path('<int:pk>/new_comment/', views.new_comment, name="new-comment"),
    path('<int:pk>/', views.QuestionPostDetail.as_view(), name="post-detail"),
    path('', views.QuestionPostList.as_view(), name="post-list"),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]