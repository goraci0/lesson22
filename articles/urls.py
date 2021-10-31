from django.contrib import admin
from django.urls import path, include
from articles import views

app_name="articles"

urlpatterns = [
    path('', views.main_page, name='index'),
    path('<int:id>', views.article_description, name='article'),
    path('add/', views.article_add, name='article_add'),
#    path('<int:id>/comment/', views.CommentListView.get_queryset(), name='comment_list'),
    path('comment/', views.CommentListView.as_view(), name='comment_list'),
    path('comment-one/<int:pk>/', views.CommentDetailView.as_view(), name='comment_one'),
    path('comment-update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment-create/', views.CommentCreateView.as_view(), name='comment_create'),
]
