def meses ():
    mes=[]
    codigo=[]
    importes=[]
    n=0
    while n!=-13:
        n=int(input("Inserte mes: "))
        while n not in range (1,13) and n!=-13:
            n=int(input("Inserte mes valido, si se quiere salir, inserte -13: "))
        if n!=-13:
            mes.append(n)
            n=int(input("Inserte codigo de operacion (1-Débito, 2-Crédito): "))
            while n not in range (1,3):
                n=int(input("Inserte codigo de operacion (1-Débito, 2-Crédito): "))
            codigo.append(n)
            n=int(input("Inserte importe: "))
            importes.append(n)
    return(mes,codigo,importes)
     
x,y,z=meses()
print(x,y,z)
for nmes in range (1,13):
    deb=float(0)
    cre=float(0)
    print("Para mes",nmes," hubieron:")
    for a in range (0,len(x)):
        if x[a]==nmes:
            if y[a]==1:
                deb+=z[a]
            if y[a]==2:
                cre+=z[a]
    print("En debito: ",deb)
    print("En credito: ",cre)
