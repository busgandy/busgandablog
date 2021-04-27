from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailViews, BlogListViews
from . import views

urlpatterns = [
    path("logout/", views.logout_request, name= "logout"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),

    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/', BlogDetailViews.as_view(), name='post_detail1'),
    path("", BlogListView.as_view(), name="base1"),
    path('home/', BlogListViews.as_view(), name='home'),
    path('base1/',BlogListView.as_view(), name= 'base'),
]