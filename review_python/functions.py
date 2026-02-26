def show_magicians(lista):
    print(lista)

def make_great(lista, aux):
    while lista:
        var = lista.pop()
        aux.append('O Grande ' + var)

lista = ['joao','nathan','pedro']
lista_nova = []
make_great(lista[:], lista_nova)
print(lista)
print(lista_nova)