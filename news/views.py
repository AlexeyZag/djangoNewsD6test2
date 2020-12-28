from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Category, Comment, Post, PostCategory, User
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm

class Posts(View):

    def get(self, request):
        posts = Post.objects.order_by('-id')
        p = Paginator(posts, 1)

        posts = p.get_page(request.GET.get('page', 1))

        data = {
            'posts': posts,
        }
        return render(request, 'posts.html', data)


class AddView(CreateView):
    template_name = 'add_article.html'
    form_class = PostForm


class AuthorsList(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.order_by('-id')

class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context

class PostDetail(DetailView):
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

class PostUpdateView(UpdateView):
    template_name = 'add_article.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SearchDetail(DetailView):
    model = Post
    template_name = 'search_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()




class Search(View):
    def get(self, request):
        posts = Post.objects.order_by('-id')
        p = Paginator(posts, 1)

        posts = p.get_page(request.GET.get('page', 1))

        data = {
            'posts': posts,
        }
        return render(request, 'search.html', data)



