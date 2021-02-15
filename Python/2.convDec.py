#222222
#Entradas:numero binario
#Salidas:numero decimal
#Reestricciones:numero binario ingresar

def convDec(x):
    z=str(x)
    temp=len(z)-1
    return decAux(z,temp,0)


def decAux(x,temp,i):
    y=x[temp]
    res=2**i
    if(x[len(x)-1]==1):
        res=1
    if(temp==0):
        res=res*int(y)
        return res
        
    else:
        res=res*int(y)
        return res+ decAux(x,temp-1,i+1)
