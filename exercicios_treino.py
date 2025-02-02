from etl import calcular_media, filtrar_acima_de, contar_valores_unicos, celsius_para_fahrenheit, calcular_desvio_padrao, encontrar_valores_ausentes

#Exec (1)
lista_valores = [5, 65, 34, 78, 943, 71, 77, 34, 55, 88, 77, 943, 65, 5, 8, 17, 22]

media_lista = calcular_media(lista_valores)

print(f"A media de valores da lista e: {media_lista:.2f}")

#Exec (2)
valores_filtrados = filtrar_acima_de(lista_valores, 70)

print(f"Os valores filtrados sao: {valores_filtrados}")


#Exec (3)
valores_unicos = contar_valores_unicos(lista_valores)

print(f"Os valores unicos das lista sao: {valores_unicos}")

#Exec (4)
limite_temperatura = filtrar_acima_de(lista_valores, 71)

temperatura_fahrenheit = celsius_para_fahrenheit(limite_temperatura)

print(f"As temperaturas convertidas para fahrenheit sao: {temperatura_fahrenheit}")

#Exec (5)
desvio_padrao_lista = calcular_desvio_padrao(lista_valores)
print(f"O desvio padrao da lista e: {desvio_padrao_lista:.2f}")

#Exec (6)
valores_ausentes = encontrar_valores_ausentes(lista_valores)
print(f"Os valores ausentes em uma sequencia sao: {valores_ausentes}")





