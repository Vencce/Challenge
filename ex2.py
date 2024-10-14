def maior_valor_dicionario(dic):
    maior_chave = None
    maior_valor = float('-inf')
    for chave, subdic in dic.items():
        for subchave, valor in subdic.items():
            if valor > maior_valor:
                maior_valor = valor
                maior_chave = (chave, subchave)
    return maior_chave, maior_valor

dicionario = {
    'A': {'x': 1, 'y': 2},
    'B': {'z': 5, 'w': 3}
}
print(maior_valor_dicionario(dicionario))
