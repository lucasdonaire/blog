# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")

from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import datetime
from django import forms

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def index(request):
    posts_list = Post.objects.all()
    context = {'post_list':posts_list}
    return render(request, 'pages/index.html', context)

def read_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pages/post.html', {'post': post})

class create_form(forms.Form):
    titulo = forms.CharField(label='titulo', max_length=200)
    livro = forms.CharField(label='livro', max_length=200)
    autor_livro = forms.CharField(label='autor_livro', max_length=200)
    conteudo = forms.CharField(label='conteudo', max_length=1e6)
def create_post(request):
    if request.method == 'POST':
        form = create_form(request.POST)
        if form.is_valid():
            post_titulo = form.cleaned_data['titulo']
            post_livro = form.cleaned_data['livro']
            post_autor_livro= form.cleaned_data['autor_livro']
            post_conteudo = form.cleaned_data['conteudo']
            post_data =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post = Post(titulo=post_titulo,
                        livro=post_livro,
                        autor_livro=post_autor_livro,
                        data=post_data,
                        conteudo=post_conteudo)
            post.save()
            return HttpResponseRedirect(
                reverse('pages:detail', args=(post.id,)))
    form = create_form(request.POST)
    return render(request, 'pages/create.html', {'form':form})

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    class update_form(forms.Form):
        titulo = forms.CharField(label='titulo', max_length=200, initial=post.titulo)
        livro = forms.CharField(label='livro', max_length=200,initial=post.livro)
        autor_livro = forms.CharField(label='autor_livro', max_length=200,initial=post.autor_livro)
        conteudo = forms.CharField(label='conteudo', max_length=1e6,initial=post.conteudo)

    if request.method == 'POST':
        form = update_form(request.POST)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.livro = form.cleaned_data['livro']
            post.autor_livro = form.cleaned_data['autor_livro']
            post.conteudo = form.cleaned_data['conteudo']
            post.save()
            return HttpResponseRedirect(
                reverse('pages:detail', args=(post.id,)))
        
    form = update_form(request.POST)
    return render(request, 'pages/update.html', {'post':post, 'form':form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('pages:index'))
    return render(request, 'pages/delete.html', {'post':post})

# def about(request):
#     context = {}
#     return render(request, 'pages/about.html', context)

# def index(request):
#     posts_list = Post.objects.all()
#     context = {'post_list':posts_list}
#     return render(request, 'pages/index.html', context)

# def read_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'pages/post.html', {'post': post})

# def create_post(request):
#     if request.method == 'POST':
#         post_titulo = request.POST['titulo']
#         post_livro = request.POST['livro']
#         post_autor_livro= request.POST['autor_livro']
#         post_data =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         post_conteudo = request.POST['conteudo']
#         post = Post(titulo=post_titulo,
#                     livro=post_livro,
#                     autor_livro=post_autor_livro,
#                     data=post_data,
#                     conteudo=post_conteudo)
#         post.save()
#         return HttpResponseRedirect(
#             reverse('pages:detail', args=(post.id,)))
#     else:
#         return render(request, 'pages/create.html', {})

# def update_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         post.titulo = request.POST['titulo']
#         post.livro = request.POST['livro']
#         post.autor_livro= request.POST['autor_livro']
#         post.conteudo = request.POST['conteudo']
#         post.save()
#         return HttpResponseRedirect(
#             reverse('pages:detail', args=(post.id,)))
#     else:
#         return render(request, 'pages/update.html', {'post':post})

# def delete_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return HttpResponseRedirect(reverse('pages:index'))
#     return render(request, 'pages/delete.html', {'post':post})