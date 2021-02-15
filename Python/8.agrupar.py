#88888888
#Entradas:un entero
#Salidas:todas las formas de agrupar los numeros
#Restricciones:ser entero

def agrupar(x):
    x=str(x)
    y=len(x)-1
    return x+' - '+bases(x,0)+' - '+juntar(x,y)

def agruparAux(x,t,y):
    z=x[t]
    res=""
    if(y==len(x)):
        return 
    
    if(t==y):
        res=res+'_'+x[y:]
        return res
    
    else:
        
        return res+z+agruparAux(x,t+1,y)
def juntar(x,y):
    uno=str(agruparAux(x,0,y))
    if(y==1):
        return uno
    else:
        return uno +" - "+ juntar(x,y-1)

def bases(x,t):
    x=str(x)
    z=x[t]
    res=""
    if(t==len(x)-1):
        res=res+z
        return res
    
    else:
        res=res+z+'_'
        return res+bases(x,t+1)
