from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Board
from .forms import BoardForm
from django.shortcuts import get_object_or_404

    
class BoardList(ListView):
    model = Board
    ordering = '-pk'

class BoardDetail(DetailView):
    model = Board
    
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
    fields = '__all__'

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