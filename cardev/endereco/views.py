from django.shortcuts import render
a = {
    'title': 'Endereço'
}
# Create your views here.

def endereco(request):
    return render(request, 'endereco/index.html', a)