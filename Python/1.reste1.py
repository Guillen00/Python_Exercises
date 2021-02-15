#111111
#Entradas:un numero
#Salidas:el numero pero con cada digito con un numero menos
#Reestricciones:entero  numero

def reste1(x):
    z=str(x)
    temp=0
    return Aux(z,temp)

def Aux(x,temp):
    y=x[temp]
    res=''
    if(int(y)==0):
        res='0'
        return res+Aux(x,temp+1)
    
    if(temp==len(x)-1):
        res= str(int(y) - 1)
        return res
    else:
        res=str(int(y) - 1)
        return res+Aux(x,temp+1)
