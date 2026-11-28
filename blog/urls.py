from blog.views import (
    BlogPostCreateView,
    BlogPostDeleteView,
    BlogPostDetailView,
    BlogPostListView,
    BlogPostUpdateView,
)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('create/', BlogPostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='post_delete'),
]
