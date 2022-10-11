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
def respcorrectas():

    vector=[]
    for i in range (0,15):
        print("Pregunta",i+1)
        n=int(input("Inserte respuesta correcta "))
        while n not in range (1,5):
            n=int(input("El valor debe ser de 1 a 4: "))
        vector.append(n)
    return(vector)

def aprobados(n,y):
    matricula=[]
    nombre=[]
    puntaje=[]
    Aprobado=0
    Reprobado=0
    for i in range (0,n):
        matri=int(input("Inserte matricula numerica"))
        matricula.append(matri)
        nom=input("Inserte nombre")
        nombre.append(nom)
        correcta=0
        vectoralumno=[]
        for i in range (0,15):
            print("Pregunta numero ",i+1)
            n=int(input("Inserte respuesta"))
            while n not in range (0,5):
                n=int(input("Inserte respuesta de entre 1 a 4"))
            vectoralumno.append(n)
        for i in range(0,15):
            if vectoralumno[i]==y[i]:
                correcta+=1
        if correcta>=9:
            puntaje.append(correcta)
            Aprobado+=1
            print("Alumno aprobado")
        else:
            puntaje.append(correcta)
            Reprobado+=1
            print("Reprobado")
        print("La matricula es",matri)
        print("Nombre es ",nom)
        print("Obtuvo",correcta,"respuestas correctas")
    return(Aprobado,Reprobado)
            
                
                
        
n=int(input("Inserte cantidad de alumnos: "))
while n<0:
    n=int(input("Inserte cantidad valida de alumnos: "))
correc=respcorrectas()

print("Las respuestas correctas son ",correc)
print("Hay",n," cantidad de alumnos ")

A,R=aprobados(n,correc)

print("Hubieron",A,"aprovados y",R,"reprobados")
