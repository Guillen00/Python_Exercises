5#3333333
#Entradas:un numero y un factor
#Salidas:la suma de cada digito multiplicado por el factor
#Reestricciones:ser enteros

def sumaMultiplos(x,y):
    z=str(x)
    temp=0
    return sumaAux(z,temp,y)

def sumaAux(z,temp,y):
    w=z[temp]
    res=0
    if(temp==len(z)-1):
        res=int(w)*y
        return res

    else:
        
        res=int(w)*y
        return res + sumaAux(z,temp+1,y)
