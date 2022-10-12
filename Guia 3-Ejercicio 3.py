def TURNO():
    t=int(input("Inserte turno "))
    while t not in range (1,3):
        t=int(input("Inserte turno valido "))
    return(t)

def CURSO():
    c=int(input("Inserte curso "))
    while c not in range (1,7):
        c=int(input("Inserte curso valido "))
    return(c)
    
def PUNTAJE():
    p=(int(input("Inserte puntaje ")))
    while p not in range (1,101):
        p=(int(input("Inserte puntaje valido ")))
    return(p)

def PROMEDIOCANTIDAD(m,t,c,p,i):
    prom=0
    cant=0
    ma=0
    ta=0
    for o in range (0,len(m)):
        if c[o]==i:
            prom+=p[o]
            cant+=1
            if t[o]==1:
                ma+=1
            if t[o]==2:
                ta+=1
    return(prom,cant,ma,ta)
            
            

    
matri=[]
turno=[]
curso=[]
puntaje=[]
n=0
a=0
while n!=-999:
    n=int(input("Inserte matricula"))
    cont=0
    if n!=-999:
        cont+=1
        print(n)
        matri.append(n)
        turno.append(TURNO())
        curso.append(CURSO())
        puntaje.append(PUNTAJE())
if cont==0:
    print("No se insertaron datos de alumnos")
for i in range (1,7):
    p,c,m,t=PROMEDIOCANTIDAD(matri,turno,curso,puntaje,i)
    if p==0 or c==0:
        a=0
    else:
        a=p/c
    print("El promedio de matematicas del curso ",i,"es: ",a," y la cantidad de alumnos en el turno mañana son son ",m," y la del turno tarde es",t)
    
    
