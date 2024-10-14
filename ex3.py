def palavras_unicas_por_chave(dic):
    unicas = {}
    for chave, lista in dic.items():
        palavras_vistas = set()
        palavras_repetidas = set()
        for palavra in lista:
            if palavra in palavras_vistas:
                palavras_repetidas.add(palavra)
            palavras_vistas.add(palavra)
        unicas[chave] = [p for p in lista if p not in palavras_repetidas]
    return unicas

dic_palavras = {
    'A': ['apple', 'banana', 'apple', 'orange'],
    'B': ['banana', 'grape', 'grape', 'apple']
}
print(palavras_unicas_por_chave(dic_palavras))
