from django.shortcuts import render, redirect
from .forms import cadProdForm
from .models import *


def cadastrarProduto(request):
    data = {}
    form = cadProdForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        data['form'] = form

    return render(request, 'produto/cadastro.html', data)


def listarProdutos(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    data['listarProdutos'] = True

    return render(request, 'produto/listar.html', data)


def listaAtualizarProdutos(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    if request.method == "POST":
        request.session['codProd'] = request.POST.get('opcaoProduto')
        return redirect('atualizar/')
    return render(request, 'produto/lista_prod_a_atualizar.html', data)

def atualizarProdutos(request):
    data = {}
    produto = Produto.objects.get(pk=request.session.get('codProd'))
    data['produto'] = produto
    form = cadProdForm(request.POST or None, instance=produto)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        data['form'] = form

    return render(request, 'produto/atualizar.html', data)

def deletarProdutos(request):
    data = {}
    data['produtos'] = Produto.objects.all()

    if request.method == 'POST':
        codProd = request.POST.get('opcaoProduto', '')
        Produto.objects.filter(codigo=codProd).delete()

    return render(request, 'produto/deletar.html', data)
