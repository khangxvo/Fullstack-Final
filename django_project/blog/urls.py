from django.urls import path
from .views import PostListView, PostDetailView
from . import views
# for testing

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    # post/<int:pk>: allow us to grab the id from url and use it as part of our url
    path('about/', views.about, name='blog-about'),
]
