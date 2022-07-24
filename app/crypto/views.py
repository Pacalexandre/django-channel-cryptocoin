""" View Root - acionando a pagina principal """
from django.shortcuts import render

def index(request):
    """index
    Args:
        request (): raiz da aplicação
    Returns:
        html:pagina com websocket de cryptocoins
    """
    return render(request, 'index.html', context={'text':'Oi mundo'})