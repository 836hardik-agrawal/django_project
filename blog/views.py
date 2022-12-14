from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts=[
    {
       'author':'CoreyMS',
       'title':'BLog post1',
       'content':'My first blog',
       'created_on':'15/10/2022',
       'college_name':'IIT BHU',


    },
     {
       'author':'Hardik agrawal',
       'title':'BLog post2',
       'content':'My second blog',
       'created_on':'15/10/2022',
       'college_name':'IIT BHU',



    }
]

def home(request):
    context= {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-created_on']
    paginate_by= 3
class UserPostListView(ListView):
    model=Post
    template_name='blog/user_post.html'
    context_object_name='posts'
    ordering=['-created_on']
    paginate_by= 3
    def get_query_set(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by(-'-created_on')


class PostDetailView(DetailView):
    model=Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','collegename']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','collegename']

    def form_valid(self,form):
        form.instance.author==self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False




    

def about(request):
    return render(request,'blog/about.html')
