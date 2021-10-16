from django.urls import path
from . import views

urlpatterns = [
    path('new_blogpost/', views.add_blog_post, name ='add_blog_post'),
    path('blogpost/<post_slug>/', views.blog_details, name ='blog_details'),
    path('drafts/', views.post_draft, name ='post_draft'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
]