"""Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""

import urllib.request

def conecta(host):
    try:
        url = host
        req = urllib.request.Request(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
        urllib.request.urlopen(req)
        # o Request faz a identificação como browser perante o site e assim o acesso fica liberado.
    except:
        return False
    else:
        return True

# Programa principal
site = 'http://www.pudim.com.br'
conecta(site)
print(f'O site {site} está acessivel.' if conecta(site) else f'O site {site} NÃO está acessível.')