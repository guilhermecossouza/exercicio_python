pessoas = [
    {"nome": "Pedro", "idade": 11},
    {"nome": "Mariana", "idade": 18},
    {"nome": "Arthur", "idade": 26},
    {"nome": "Rebeca", "idade": 6},
    {"nome": "Thiago", "idade": 19},
    {"nome": "Gabriela", "idade": 17},
]

menores = filter(lambda p: p["idade"] < 18, pessoas)
print(list(menores))
print("-="*30)
maiores = filter(lambda p: p["idade"] >= 18, pessoas)
print(list(maiores))
print("-="*30)
nomes_longos = filter(lambda p: len(p["nome"]) > 6, pessoas)
print(list(nomes_longos))
