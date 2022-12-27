from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Board, Board_Comment
from .forms import BoardForm, CommentForm
from django.shortcuts import get_object_or_404


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Board_Comment
    form_class = CommentForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
            
        else:
            raise PermissionDenied
    
class BoardList(ListView):
    model = Board
    ordering = '-pk'
    paginate_by = 10

class BoardDetail(DetailView):
    model = Board
    
    def get_context_data(self, **kwargs):
        context = super(BoardDetail,self).get_context_data()
        context['comment_form'] = CommentForm
        return context    
    

class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardForm
    
    def form_valid(self,form):
        current_user = self.request.user
        
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(BoardCreate, self).form_valid(form)
            return response
        
        else:
            return redirect('/board/')
        
        
class BoardUpdate(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['title', 'content']

    template_name = 'board/board_update_form.html'
    
    def get_context_data(self, **kwargs):
        context = super(BoardUpdate, self).get_context_data()

        return context
    
    def form_valid(self, form):
        response = super(BoardUpdate, self).form_valid(form)

        return response
       
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(BoardUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def delete_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user.is_authenticated and request.user == board.author:
        board.delete()
        
    return redirect('/board/')


def new_comment(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)
        
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.board = board
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            
        else:
            return redirect(board.get_absolute_url())
    
    else:
        raise PermissionDenied
        
def delete_comment(request, pk):
    comment = get_object_or_404(Board_Comment, pk=pk)
    board = comment.board
    
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(board.get_absolute_url())
    
    else:
        raise PermissionDenied