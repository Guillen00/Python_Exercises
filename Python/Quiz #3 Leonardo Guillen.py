#Entradas: un digito y un nunmero entero
#Salidas:2 numeros uno con los numeros menores y otro con los mayores
#Restricciones:ser enteros

#1
def divida(x,y):
    y=str(y)
    return dividaAux(x,y,0)

def dividaAux(x,y,temp):
    z=y[temp]
    Menores=""
    Mayores=""
    if(temp==len(y)-1):
        if(int(z)<x):
            Menores=Menores+str(z)
            return Menores,Mayores
        else:
            Mayores=Mayores+str(z)
            return Menores,Mayores
    if(int(z)<x):
        Menores=Menores+str(z)
        return Menores+dividaAux(x,y,temp+1)
    else:
        Mayores=Mayores+str(z)
        return Menores+dividaAux(x,y,temp+1)

#2
def separar(lista):
    temp=0
    listafinal=[]
    listafinal.append(separarAux(lista,temp))
    print(listafinal)


def separarAux(lista,temp):
    x=lista[temp]
    Primos=[]
    Noprimos=[]
    if(temp==len(lista)-1):
        if(primo(x)==True):
            Primos.append(x)
            return Primos,Noprimos
        else:
            Noprimos.append(x)
            return Primos,Noprimos
    if(primo(x)==True):
            Primos.append(x)
            return Primos+separarAux(lista,temp+1)
    else:
        Noprimos.append(x)
        return Noprimos+separarAux(lista,temp+1)

def primo(x):
    if(x==1 or x==2 or x==3 or x==5 or x==7 or x==11):
        return True
    else:
        if(x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0):
            return False
        else:
            return True
