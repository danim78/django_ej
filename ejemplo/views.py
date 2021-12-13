from django.shortcuts import render

# Create your views here.

def noticia_list(request):
    template = "ejemplo/noticia_list.html"
    return render(request, 'ejemplo/noticia_list.html', {})
