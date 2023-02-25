from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categoria = ['casa', 'carro', 'moto', 'apartamento']
    context = {'name' : name, 'categoria': categoria, }
    return render(request, 'dinamico.html', context)
