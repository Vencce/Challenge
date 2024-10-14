def aninhamento_de_chaves(chaves):
    resultado = {}
    atual = resultado
    for chave in chaves:
        atual[chave] = {}
        atual = atual[chave]
    return resultado

chaves = ['a', 'b', 'c', 'd']
print(aninhamento_de_chaves(chaves))
