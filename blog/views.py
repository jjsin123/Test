# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView): # 클래스를 사용하면 index역할을 하기 때문에 
    model = Post        #아래의 긴 코드와 같은 결과를 간단하게 표현 가능하다.
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
    # templates_name = 'blog/index.html'

# from django.shortcuts import render
# from .models import Post



# def index(request):
    
#     posts = Post.objects.all().order_by('-pk')
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

# def single_post_page(request,pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )

# Create your views here.
