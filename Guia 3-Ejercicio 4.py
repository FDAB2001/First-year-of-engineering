def importes():
    i=int(input("Inserte importe de la compra: "))
    return(i)

def codigos ():
    i=int(input("Inserte codigo de la compra: "))
    while i not in range (1,4):
        i=int(input("Inserte codigo de la compra: "))
    return(i)


sucursal=[]
importe=[]
codigo=[]

n=0
while n!=-99:
    n=int(input("Inserte sucursal "))
    while n not in range (1,16) and n!=-99:
        n=int(input("Inserte sucursal valida "))
    if n!=-99:
        sucursal.append(n)
        importe.append(importes())
        codigo.append(codigos())


for i in range (1,16):
    tefec=0
    tche=0
    ttar=0
    cont=0
    
    for a in range (0,len(sucursal)):
        if i==sucursal[a]:
            cont+=1
            if codigo[a]==1:
                tefec+=importe[a]
            if codigo[a]==2:
                tche+=importe[a]
            if codigo[a]==3:
                ttar+=importe[a]
    if cont==0:
        print("La sucursal",i,"no tuvo ventas")
    else:
        print("El numero de la sucursal es: ",i)
        print("El total de efectivo es",tefec,"el total del cheque es ",tche,"el total de tarjetas es ",ttar,"y el total de las transacciones es",ttar+tche+ttar)
