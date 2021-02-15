def binarios(y):
    if isinstance(y,int):
        return binariosAux(y)

def binariosAux(y):
    if(y==0):
        return ""
    else:
        primer=y//10**(len(str(y))-1)
        rep=ocurrencias(y,primer)
        res=convBin(rep)
        rest=ceros(res,len(res)-1)
        return rest+" " +  binariosAux(erase(y,primer))

def ocurrencias(y,a):
    if(y==0):
        return 0
    else:
        if(y%10==a):
            return 1+ ocurrencias(y//10,a)
        else:
            return ocurrencias(y//10,a)
    
def convBin(y):
    if(y==0):
       return ""
    else:
        return convBin(y//2) + str(y%2)

def erase(y,a):
    if isinstance(a,int):
        return eraseAux(y,a,0)
    else:
        return "Error"

def eraseAux(y,a,c):
    if(y==0):
        return 0
    else:
        if(y%10==a):
            return eraseAux(y//10,a,c)
        else:
            return (y%10)*10*c+eraseAux(y//10,a,c+1)


def ceros(x,y):    #x numero, y len(X)-1,2 == espacios por querer #-1 o sea 2
    if(y==2):
        return x
    else:
        res='0' 
        return  res + str(ceros(x,y+1))
