def comprimir_dicionario(dic, limite):
    return {chave: valor for chave, valor in dic.items() if valor >= limite}

dic = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
limite = 10
print(comprimir_dicionario(dic, limite))
