#Se desea implementar un algoritmo que registre las temperaturas de un día. Para ello se
#deben ingresar los siguientes valores: DIA, MES, AÑO y 12 DATOS correspondientes a las
#temperaturas de ese día, tomadas a intervalos de 2 horas. Calcular la TEMPERATURA MEDIA
#del día e imprimirla junto con la FECHA de ese día.

def fecha ():
    vector=[]
    vector2=[]
    vector3=[]
    n=int(input("Inserte dia: "))
    while n not in range (1,32):
        n=int(input("Inserte dia valido: "))
    vector.append(n)
    n=int(input("Inserte mes: "))
    while n not in range (1,12):
        n=int(input("Inserte mes valido: "))
    vector2.append(n)
    n=int(input("Inserte año: "))
    vector3.append(n)
    return (vector,vector2,vector3)
def temperaturas ():
    vector=[]
    suma=0
    for i in range(0,25,2):
        print("Inserte temperatura a las ",i,"horas")
        n=float(input())
        vector.append(n)
        suma+=n
    return(vector,suma)
    
print("Programa para calcular la temperatura media: ")
x,y,z=fecha()
print("La fecha a analizar es ",x[0],"/",y[0],"/",z[0])
temp,men=temperaturas ()
print("Las temperaturas fueron",temp)
print("La media de dichas temperaturas es",men/12)
