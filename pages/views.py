# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")

from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# from .forms import ReviewForm
from django.urls import reverse
from django.views import generic
from datetime import datetime


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

def create_post(request):
    if request.method == 'POST':
        post_titulo = request.POST['titulo']
        post_livro = request.POST['livro']
        post_autor_livro= request.POST['autor_livro']
        post_data =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        post_conteudo = request.POST['conteudo']
        post = Post(titulo=post_titulo,
                    livro=post_livro,
                    autor_livro=post_autor_livro,
                    data=post_data,
                    conteudo=post_conteudo)
        post.save()
        return HttpResponseRedirect(
            reverse('pages:detail', args=(post.id,)))
    else:
        return render(request, 'pages/create.html', {})

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.livro = request.POST['livro']
        post.autor_livro= request.POST['autor_livro']
        post.conteudo = request.POST['conteudo']
        post.save()
        return HttpResponseRedirect(
            reverse('pages:detail', args=(post.id,)))
    else:
        return render(request, 'pages/update.html', {'post':post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('pages:index'))
    return render(request, 'pages/delete.html', {'post':post})