def mesclar_dicionarios(dic1, dic2):
    resultado = dic1.copy()
    for chave, valor in dic2.items():
        if chave in resultado:
            resultado[chave] += valor
        else:
            resultado[chave] = valor
    return resultado

dic1 = {'a': 10, 'b': 20, 'c': 30}
dic2 = {'b': 5, 'c': 15, 'd': 25}
print(mesclar_dicionarios(dic1, dic2))
