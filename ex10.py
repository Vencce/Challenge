def mapear_palavras(texto, mapa_substituicao):
    palavras = texto.split()
    resultado = [mapa_substituicao.get(palavra, palavra) for palavra in palavras]
    return ' '.join(resultado)

texto = "apple banana orange"
mapa_substituicao = {'apple': 'fruit', 'banana': 'yellow'}
print(mapear_palavras(texto, mapa_substituicao))
