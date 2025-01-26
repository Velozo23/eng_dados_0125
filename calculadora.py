valor1 = 8
valor2 = 7

valor4 = 8
valor5 = 5

def soma(primeiro_valor: float, segundo_valor: float)-> float:
    '''
    uma funcao simples, de soma do tipo float que retorna float
    '''
    resultado_soma = primeiro_valor + segundo_valor
    return resultado_soma


valor3 = soma(primeiro_valor = valor1, segundo_valor=valor2 )
valor6 = soma(valor4, valor5)

print(valor3)
print(valor6)

