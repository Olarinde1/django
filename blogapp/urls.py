from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView,BlogCommentView

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name='post_edit'),
    path("post/new/", BlogCreateView.as_view(), name='post_new'),
    path("", BlogListView.as_view(), name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post_detail'),
    # path('<slug:slug>/', post_detail, name='post_detail'),
    path("post_comment/<int:pk>/", BlogCommentView.as_view(), name='post_comment'),
]
