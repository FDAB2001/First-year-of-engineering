#muy largo pero le vas a cachar
def Mes():
    n=1
    NumeroMes=[]
    Importe=[]
    while n!=-99:
        n=int(input("Inserte mes: "))
        if n!=-99:
            while n not in range (0,13) and n!=-99:
                print("El mes no puede ser negativo ni mayor a 12, si se desea salir del loop, insertar -99")
                n=int(input("Inserte mes: "))
            if n!=-99:
                NumeroMes.append(n)
                a=int(input("Inserte Importe: "))
                while a<0:
                    print("El importe no puede ser negativo")
                    a=int(input("Inserte Importe: "))
                Importe.append(a)
    return(NumeroMes,Importe)

def ordenar(M,I):
    cambio=0
    while cambio==0:
        for i in range(0,len(I)-1):
            aux=I[i]
            if aux>I[i+1]:
                I[i]=I[i+1]
                I[i+1]=aux
                aux=M[i]
                M[i]=M[i+1]
                M[i+1]=aux
                cambio+=1
        if cambio!=0:
            print("Se realizaron ",cambio,"cambios en la vuelta")
            cambio=0
        else:
            cambio=1
    return(M,I)     

def ordenarMes(M,I):
    cambio=0
    while cambio==0:
        for i in range(0,len(M)-1):
            aux=M[i]
            if aux>M[i+1]:
                M[i]=M[i+1]
                M[i+1]=aux
                aux=I[i]
                I[i]=I[i+1]
                I[i+1]=aux
                cambio+=1
        if cambio!=0:
            print("Se realizaron ",cambio,"cambios en la vuelta")
            cambio=0
        else:
            cambio=1
    return(M,I)     




M,I=Mes()
print("Lista de meses",M)
print("Lista de ventas",I)
print("¿Desea ordenar las ventas de menor a mayor?")
n=int(input("Para Si presione 1 para No precione 0"))
if n==1:
    M,I=ordenar(M,I)
    print("Lista de meses ordenados",M)
    print("Lista de ventas ordenados de menor a mayor",I)
print("¿Desea ordenar los meses de menor a mayor?")
n=int(input("Para Si presione 1 para No precione 0"))
if n==1:
    M,I=ordenarMes(M,I)
    print("Lista de meses ordenados",M)
    print("Lista de ventas",I)
del n
