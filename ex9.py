def dicionario_de_matrizes(matriz):
    dic_matriz = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            dic_matriz[(i, j)] = valor
    return dic_matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(dicionario_de_matrizes(matriz))
