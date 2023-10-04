import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def aumentar(preco=0.00, porcentagem=0.00, formatado=False):
    aumento = (preco * porcentagem) / 100
    print(f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco + aumento):.2f}")


def diminuir(preco=0.00, porcentagem=0.00, formatado=False):
    valor = (preco * porcentagem) / 100
    print(f"O valor informado foi de R${preco:.2f}, aumentou {porcentagem}% e foi para R${(preco - valor):.2f}")

def dobro(valor=0.00, formatado=False):
    dobrar = valor * 2
    print(f"O valor informado foi de {valor:.2f} dobrado foi para R${dobrar:.2f}")

def metade(valor=0.00, formatado=False):
    metade = valor / 2
    print(f"O valor informado foi de R${valor:.2f} e sua metade é R${metade:.2f}")

def moeda(valor=0.00, formatado=False):    
    valor = locale.currency(valor, grouping=True, symbol="R$")
    print(valor)
    