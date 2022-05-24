#INSTRUCCIONES
#Ingrese la ubicación cocina/cine/restaurante en letras minúscula
#Ingrese el condimento sal si desea como "si" o si no desea como "no" en minúscula
#Ingrese el estado O/1 en consecuencia, donde 0 significa PALOMITAS y 1 significa MAIZ CANGUIL

def canguilera():
    #inicializador del estado de objetivo
    estado_de_objetivo = {'cocina': '0','cine':'0', 'restaurante':'0'}
    costo = 0
    #Condimento para las palomitas
    componentes = {'sal':'si', 'sin_sal':'no'}

    #El usuario ingresa la ubicación de dónde está situada la canguilera
    ubicacion_entrada = input ("Ingrese la ubicación de la canguilera: ") 
    #El usuario ingresa si en la ubicación ya están las palomitas o están por hacer
    estado = input ("Ingrese el estado del canguil en la "+ubicacion_entrada+": ")
    componentes = input("Desea agregar sal: ")

    if ubicacion_entrada == 'cocina':
        print("La canguilera está en la cocina")
        #En la ubicación cocina no está listo las palomitas
        if estado == '1':
            print("El maiz canguil listo para ser palomitas")
            #Se agrega el condimento sal
            if componentes == 'si':
                print("Se agrega sal")
                #El costo incrementa por la agregación del condimento
                costo +=1
            #No se agrega el condimento sal 
            elif componentes == 'no':
                print("Sin sal")
            #Mensaje de activación del sistema de cocción proceso previo para la obtención de las palomitas
            print("Activación del sistema de cocción por aire")
            estado_de_objetivo ['cocina']= '0'
            #Incrementa por las palomitas lista en la cocina
            costo +=1 
            print("Las palomitas ya están listas")
            print("Costo ACtual: "+ str(costo))
        else:

            print("En la ubicación cocina ya están listas las palomitas")
            print("No existieron nuevos costos")

        print("Medición del desempeño: "+ str(costo))

    elif ubicacion_entrada == 'cine':
        print("La canguilera está en el cine")
         #En la ubicación cine no está listo las palomitas
        if estado == '1':
            print("El maiz canguil listo para ser palomitas")
            #Se agrega el condimento sal
            if componentes == 'si':
                print("Se agrega sal")
                #El costo incrementa por la agregación del condimento
                costo +=1
            #No se agrega el condimento sal 
            elif componentes == 'no':
                print("Sin sal")
            #Mensaje de activación del sistema de cocción proceso previo para la obtención de las palomitas
            print("Activación del sistema de cocción por aire")
            estado_de_objetivo ['cine']= '0'
            costo +=1
            print("Las palomitas ya están listas")
            print("Costo ACtual: "+ str(costo))
        else:
            print("En la ubicación cine ya están listas las palomitas")
            print("No existieron nuevos costos")

    elif ubicacion_entrada == 'restaurante':
        print("La canguilera esta en el restaurante")
        #En la ubicación restaurante no está listo las palomitas
        if estado == '1':
            print("El maiz canguil listo para ser palomitas")
            #Se agrega el condimento sal
            if componentes == 'si':
                print("Se agrega sal")
                costo +=1
            #No se agrega el condimento sal 
            elif componentes == 'no':
                print("Sin sal")
            print("Activación del sistema de cocción por aire")
            estado_de_objetivo ['restaurante']= '0'
            costo +=1
            print("Las palomitas ya están listas")
            print("Costo ACtual: "+ str(costo))
        else:
            print("En la ubicación restaurante ya están listas las palomitas")
            print("No existieron nuevos costos")

canguilera()  