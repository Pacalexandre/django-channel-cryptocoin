""" View Root - acionando a pagina principal """
from django.shortcuts import render

def index(request):
    """index
    Args:
        request (): raiz da aplicação
    Returns:
        html:pagina com websocket de cryptocoins
    """
    #esse codigo foi movido para tasks que vai fazer essa carga atravez do websocket 
    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    # coins = requests.get(url).json()
    # return render(request, 'index.html', context={'text':coins})
    return render(request, 'index.html')