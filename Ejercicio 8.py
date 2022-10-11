#Leer N que representa la cantidad de alumnos que rindieron un Test de Aptitud para el
#Ingreso a la Universidad. Se desea desarrollar un algoritmo para realizar la Corrección
#Automática del Test que consta de 15 preguntas de selección múltiple.
#Para esto se leerá inicialmente un VECTOR CON LAS RESPUESTAS CORRECTAS que servirá
#como corrector (valores posibles de respuesta 1 a 4). Y a continuación se leerán N veces los
#datos de cada alumno en la forma siguiente:
#• No de Matrícula (la matrícula es numérica)
#• Nombre
#• un Vector de 15 elementos que contiene las 15 respuestas que dio a cada una de
#las 15 preguntas del test.

#Para corregir se debe comparar el vector de Respuestas del Alumno con el vector de
#Respuestas Correctas para acumular el total de respuestas correctamente contestadas por
#cada alumno y entonces imprimir su No de Matrícula, su Nombre y la CANTIDAD de
#Respuestas Correctas que obtuvo y un MENSAJE de “Aprobado” o “Reprobado” según si el
#TOTAL DE RESPUESTAS CORRECTAS (con 9 o más respuestas correctas es considera
#APROBADO).
#Al final se desea saber la CANTIDAD DE APROBADOS y la CANTIDAD DE REPROBADOS del
#Test.
def ordenar(vector):
    cambio=0
    while cambio==0:
        for i in range(0,len(vector)-1):
            aux=vector[i]
            if aux>vector[i+1]:
                vector[i]=vector[i+1]
                vector[i+1]=aux
                cambio+=1
        if cambio!=0:
            cambio=0
        else:
            cambio=1
    return(vector)    
vectorA=[]
vectorB=[]
for i in range (0,int(input("Inserte cantidad de componentes"))):
    vectorA.append(i)
    vectorB.append(i)
vectorC=[]
for i in range (0,len(vectorA)*2):
    vectorC.append(len(vectorA)*2-i)
print(vectorC)
vectorC=ordenar(vectorC)
print(vectorC)
