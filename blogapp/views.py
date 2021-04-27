from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


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
        form\
            = UserCommentForm()
    return render(request, 'post_comment.html', {'form':form})