diccionario={
    # 'nombre': "Gabriel",
    # 'edad': 18,
    # 'HinchaVerde': True,
    # 'ComidaFavorita':['Hamburguesa','pan']
}
diccionario['nombre']=input("Digite su nombre: ")

print(diccionario)
print(diccionario['nombre'])

for llave,valor in diccionario.items():
    print(llave)
    print(valor)