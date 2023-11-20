from .models import Post, Comment, Category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from datetime import datetime
from django import forms
import django.views.generic.edit as Generics


class create_form(forms.Form):
    titulo = forms.CharField(label='titulo', max_length=200)
    livro = forms.CharField(label='livro', max_length=200)
    autor_livro = forms.CharField(label='autor_livro', max_length=200)
    conteudo = forms.CharField(label='conteudo', max_length=1e6)
class index(generic.ListView):
    model = Post
    template_name = 'pages/index.html'

class read_post(generic.DetailView):
    model = Post
    template_name = 'pages/post.html'
    context_object_name = 'post'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(post_id=context['post'].id).order_by('-data')
        return context

class create_post(generic.CreateView):
    model = Post
    template_name = 'pages/create.html'
    fields = ['titulo', 'livro', 'autor_livro', 'conteudo']
    def get_success_url(self):
        return reverse('pages:detail', kwargs={'post_id': self.object.id})
    
class update_post(generic.UpdateView):
    model = Post
    template_name = 'pages/update.html'
    fields = ['titulo', 'livro', 'autor_livro', 'conteudo']
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    def get_success_url(self):
        return reverse('pages:detail', kwargs={'post_id': self.object.id})

class delete_post(generic.DeleteView):
    model = Post
    template_name = 'pages/delete.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    def get_success_url(self):
        return reverse('pages:index')

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

class create_comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','texto']
        labels = {'author': 'Usuário','texto': 'Comentário'}

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = create_comment_form(request.POST)
        if form.is_valid():
            comment_texto = form.cleaned_data['texto']
            comment_author = form.cleaned_data['author']
            comment = Comment(texto=comment_texto,author=comment_author, post_id=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('pages:detail', args=(post.id,)))
    form = create_comment_form(request.POST)
    return render(request, 'pages/create_comment.html', {'form':form,'post':post})

class categoryListView(generic.ListView):
    model = Category
    template_name = 'pages/categorys.html'

class categoryDetailView(generic.DetailView):
    model = Category
    template_name = 'pages/detail_category.html'
    
class categoryCreateView(generic.CreateView):
    model = Category
    template_name = 'pages/create_category.html'
    fields = ['name', 'description', 'posts']
    success_url = reverse_lazy('pages:categorys')