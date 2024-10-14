def dicionario_circular(chaves):
    dic = {}
    for i in range(len(chaves)):
        proxima_chave = chaves[(i + 1) % len(chaves)]
        dic[chaves[i]] = proxima_chave
    return dic

chaves = ['a', 'b', 'c', 'd']
print(dicionario_circular(chaves))
