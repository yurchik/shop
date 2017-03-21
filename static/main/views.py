from django.shortcuts import render


def index(request):
    context = {
        'var': 'Test1',
    }
    return render(request, 'main/index.html', context)
