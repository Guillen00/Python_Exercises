#Ejercicio de recursion compleja

#Entrada: Un numero x
#Salida: Un string con la suma de cada ocurrencia de un numero dentro de x
#Restricciones: Lo que se ingresa es un int

def encontrar(x,y,z):
    if(len(x)==0):
        return False
    if(z==len(x)):
       return False
    elif(x[z] == y):
        return True
    else:
        return encontrar(x,y,z+1)

        
def ocurrencias(x,res,i):
    if(i==len(x)-1):
        if(encontrar(res,x[i],0)== False):
            res = res + x[i]
        return res
    elif(encontrar(res,x[i],0)):
        return ocurrencias(x,res,i+1)
    else:
        res = res + x[i]
        return ocurrencias(x,res,i+1)
        
def sumaRep(x,o,i,res):
    if(i==len(x)-1):
        if(x[i] == o):
           res = res + int(o)
        return res
    elif(x[i] == o):
        res = res + int(o)
        return sumaRep(x,o,i+1,res)
    else:
        return sumaRep(x,o,i+1,res)
        
def main(x):
    if(len(str(x))==1):
        return str(x)
    else:
        return main_aux(str(x),0,"")

def main_aux(x,i,rf):
    ocur = ocurrencias(x,"",0)
    if(i==len(ocur)-1):
        rf = rf + " " + str(sumaRep(x,ocur[i],0,0))
        return rf
    else:
        return main_aux(x,i+1, rf + " " + str(sumaRep(x,ocur[i],0,0)))
