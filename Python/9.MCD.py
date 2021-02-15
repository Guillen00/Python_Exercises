#999999999
#Entradas:dos numeros
#Salidas:el maximo comun multiplo de esos valores
#Reestricciones:valores enteros


def MCD(a,b):
    return MCDAux(a,b)

def MCDAux(a,b):
    res=1
    if(a%2==0 and b %2==0):
        res=res*2
        return  res*MCDAux(a/2,b/2)
    if(a%3==0 and b %3==0):
        res=res*3
        return  res*MCDAux(a/3,b/3)
    if(a%5==0 and b %5==0):
        res=res*5
        return  res*MCDAux(a/5,b/5)
    if(a%7==0 and b %7==0):
        res=res*7
        return  res*MCDAux(a/7,b/7)
    if(a%11==0 and b %11==0):
        res=res*11
        return  res*MCDAux(a/11,b/11)
    else:
        return res


