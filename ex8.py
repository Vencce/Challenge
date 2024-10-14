def ordenar_por_valor(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

dic = {'a': 10, 'b': 5, 'c': 20, 'd': 3}
print(ordenar_por_valor(dic))
