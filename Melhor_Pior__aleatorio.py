import timeit
from random import randint
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt


def desenhaGrafico(x, y, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('grafico_melhor.png')


swap = []


def bubble_sort(lista):
    swaps = 0
    elementos = len(lista) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            swaps += 1
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
    return swaps


x = [1000, 2000, 4000, 6000]
y = []


def geralistadecres(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam -= 1
    return lista


def geralistacres(tam):
    lista = []
    x = 1
    while x <= tam:
        lista.append(x)
        x += 1
    return lista


def geraLista(tam):
    lista = []
    while tam > len(lista):
        n = randint(1, 1 * tam)
        if n not in lista: lista.append(n)
    return lista


for i in range(4):
    lista = geralistacres(x[i])
    y.append(timeit.timeit("bubble_sort({})".format(lista), setup="from __main__ import bubble_sort", number=1))
    swap.append(bubble_sort(lista))

# para gerar o grafico do tempo de ordenacao do bubble sort
desenhaGrafico(x, y)
# para gerar o grafico do numero de verificacoes em cada ordenacao
# desenhaGrafico(x,swap)
