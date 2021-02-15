#666666666
#Entradas:numero entero
#Salidas:en numeros binarios la cantidad de recursiones de cada numero en binario
#Restricciones:que sea un entero


def binarios(y):
    x=str(y)
    return bin1(ocurrencias(bases(y,0,0,0),1,0))



def bin1(x):
    res=''
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
    
             

def ocurrencias(x,r,temp):
    z=x[temp]
    res=0
    if(temp==len(x)-1):
        if(int(z)==r):
            res=res+1
            return res
        else:
            return res
    else:
        if(int(z)==r):
            res=res+1
            return res+ocurrencias(x,r,temp+1)
        else:
            return res+ocurrencias(x,r,temp+1)

def bases(w,q,temp,z):
    w=str(w)
    c=w[temp]
    res=""
    if(temp==len(w)-1):
        if(q==9):
            if(int(c)==z):
                res=res+str(z)
                return res
            if(z==10):
                return res
            else:
                return res+bases(w,q,temp,z+1)
        else:
            temp=0
            return res + bases(w,q+1,temp,z)
        
    else:
        if(c==str(q)):
            res=res+c
            temp=0
            return res + bases(w,q+1,temp,z)
        else:
            return res+bases(w,q,temp+1,z)
#bin1 ocupa ocurrencias,ocurrencias necesita dato y numero ,bases necesita nada

