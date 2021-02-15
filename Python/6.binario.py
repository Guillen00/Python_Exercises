#666666666
#Entradas:numero entero
#Salidas:en numeros binarios la cantidad de recursiones de cada numero en binario
#Restricciones:que sea un entero


def binarios(y):
    if isinstance(y,int):
        x=str(y)
        return binAux(x,1)
    else:
        print("Error no es numero entero")


def binAux(y,a):
    if(a==10):
        return ''
    p=bin1(ocurrencias(y,a))
    if(p==000):
        return binAux(y,a+1)
    b=ceros(p,len(p)-1)
    return str(b)+' '+ str(binAux(y,a+1))
    



def bin1(x):
    res=''
    if(x==0):
        return 0
    if(x<=7):
        if(x<2):
            res='1'+res
            return res
        if(x%2==0):
            res='0'+res
            return bin1(x/2)+res
        else:
            res='1'+res
            return bin1((x-1)/2)+res
    
def ceros(x,y):    #x numero, y len(X)-1,u meta 3
    if(y==2):
        return x
    else:
        res='0' 
        return  res + str(ceros(x,y+1))

def ocurrencias(y,a):
    if(y==0):
        return 0
    else:
        if(int(y)%10==a):
            return 1+ ocurrencias(int(y)//10,a)
        else:
            return ocurrencias(int(y)//10,a)





#bin1 ocupa ocurrencias,ocurrencias necesita dato y numero ,bases necesita nada

