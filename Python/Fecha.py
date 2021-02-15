def fechaVuelta():
    print("Escriba la fecha de salida en formato dia/mes/ano  00/00/0000")
    a=input("")
    x=int(a[:2])
    y=int(a[3:-5])
    z=int(a[-4:])
    print(x,y,z)

    print("Escriba la fecha de entrega en formato dia/mes/ano  00/00/0000")
    b=input("")
    c=int(b[:2])
    d=int(b[3:-5])
    e=int(b[-4:])
    print(c,d,e)

    dias=(x-c)+((y-d)*30)+(((z-e)*12)*30)
    
    print(abs(dias))
