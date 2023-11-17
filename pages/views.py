from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
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
