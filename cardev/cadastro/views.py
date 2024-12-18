from django.shortcuts import render
a = {
    'title': 'Cadastro'
}
# Create your views here.

def cadastro(request):
    return render(request, 'cadastro/index.html', a)