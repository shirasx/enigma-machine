def rotorRotacao(lista):
    lista.append(lista[0])
    del lista[0]
    return lista