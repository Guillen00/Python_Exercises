#10
#Entradas:un numero
#salidas:una piramide con el numero ingresado de niveles
#Restricciones:ser mayor que 0 y ser entero

def triangulo(x):
    return trianguloAux(x,1,x-1)

def trianguloAux(x,temp,esp):
    res=" \n"
    if(x==0):
        return ' '
    if(x==temp):
        res=res+cont(temp)
        return print(res)
    else:
        z=espacios(1,esp)
        res=res+(z+cont(temp))
        return print(res),trianguloAux(x,temp+1,esp-1)


def cont(x):
    res=""
    if(x==0):
        return res
    else:
        res=res+"*   " 
        return res+cont(x-1)

def espacios(esp,temp): #0,x-1
    res=""
    if(esp==temp):
        res=res+"  "
        return res
    else:
        res=res+"  "
        return res+espacios(esp+1,temp)
