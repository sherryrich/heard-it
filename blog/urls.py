from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('about', views.generic.TemplateView.as_view(template_name='about.html'), name='about'),
    path('search_articles', views.search_articles, name='search_articles'),
    path('new', views.CreatePostView.as_view(), name='new'),
    path('<slug:slug>/update/', views.UpdatePostView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
