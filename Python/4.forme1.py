#4444444444
#Entradas:
#Salidas:
#Restricciones:


def forme1(y):
    x=str(y)
    return formeAux(x,0)

def formeAux(x,t):
    y=x[t]
    res=''
    if(t==len(x)-1):
        if(int(y)==1):
            res=res+'1'
            
            return res
        else:
            
            return res
    if(int(y)==1):
        
        res=res+'1'
        
        return res+ formeAux(x,t+1)
    else:
        return res+ formeAux(x,t+1)
