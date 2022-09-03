print("****MENU****")
print("1. Agregar 1 empanada")
print("2. Mostrar Empanada")
print("3. SALIR")
opcion=100
eleccion=""
#DATOS EMPANADA
#SABOR
#INGREDIENTES(X3)
#PRECIO FABRICACION
#PRECIO VENTA
empanada={}
ingredientes=[]

while(opcion!=3):
    opcion=int(input("Digite una opción: "))
    if(opcion==1):
        empanada['sabor']=input("Digite su sabor: ")
        for i in range(3):
            ingredientes.append(input("Digite el nombre del ingrediente: "))
        empanada['ingredientes']=ingredientes
        empanada['precioFabricacion']=input("Digite el precio de la fabricacion")
        empanada['precioVenta']=input("Digite el precio de la venta")
        print("Agregando empanada")
    elif(opcion==2):
        print(empanada)
    elif(opcion==3):
        break
    else:print("La opcion ingresada no fue válida")
