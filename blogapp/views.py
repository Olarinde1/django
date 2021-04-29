from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    # context_object_name = 'posts'
    ordering = ['-date_created']


class UserBlogListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    # context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_created")


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogCommentView(CreateView):
    model = Comment
    template_name = 'post_comment.html'
    fields = ['user', 'email', 'created_on', 'comment']


def comment(request):
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail')
    else:
        form = UserCommentForm()
    return render(request, 'post_comment.html', {'form': form})
