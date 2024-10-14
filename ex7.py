def frequencia_palavras(texto):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

texto = "apple banana apple orange banana banana"
print(frequencia_palavras(texto))
