#Leer un vector A de N componentes y crear tres variables R , S y T que indiquen:
#R cuántas componentes del vector son menores o iguales que 5
#S cuántas componentes del vector son mayores que 5 pero menores que 12
#T cuántas componentes del vector son mayores o iguales que 12
#Imprimir las tres variables creadas y también el PROMEDIO de los números que
#cumplieron cada una de las condiciones.
def promedio(r):
    prom=0
    for i in range (0,len(r)-1):
        prom+=r[i]
    print("El promedio de la primera condicion es:",prom/len(r))
    return(prom)

def promedio(s):
    prom1=0
    for i in range (0,len(s)-1):
        prom1+=s[i]
    print("El promedio de la segunda condicion es:",prom1/len(s))
    return(prom1)

def promedio(t):
    prom2=0
    for i in range (0,len(t)-1):
        prom2+=t[i]
    print("El promedio de la tercera condicion es:",prom2/len(t))
    return(prom2)
vector=[]
n=int(input("Inserte dimension "))
for i in range (0,n):
    vector.append(int(input("inserte componente")))
print(vector)

r=list()
s=list()
t=list()
for i in range (0,n):
    for i in range(0,n-1):
        aux=vector[i]
        o=0
        if aux>vector[i+1]:
            vector[i]=vector[i+1]
            vector[i+1]=aux
            o+=1
for i in range (0,n):
    if vector[i]<=5:
            r.append(vector[i])
    if vector[i]>=5 and vector[i]<12:
            s.append(vector[i])
    if vector[i]>=12:
            t.append(vector[i])

print("Las componentes menores que 5 son",len(r))
print("Las componentes mayores que 5 pero menores que 12 son",len(s))
print("Las componentes mayores o iguales a 12 son",len(t))
print(vector)
if len(r)!=0:
    a=promedio(r)
if len(s)!=0:
    b=promedio(s)
if len(t)!=0:
    c=promedio(t)
if len(r)==0 or len(s)==0 or len(t)==0:
    print ("Una de las variables no tiene componentes, asi que no se imprime")
