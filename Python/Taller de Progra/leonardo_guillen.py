#1
#Entradas:Un número entero
#Salidas:el producto factorial
#Restricciones:lo ingresado debe ser un número y que sea entero

def factorial(x):
    res=1
    while(x>0):
        res=res*x
        x=x-1
    return res

#2
#Entradas:un número entero
#Salidas:los números pares
#Restricciones:ser número entero

def forma_par(x):
    x=str(x)
    i=0
    res=""
    while(i>len(x)):
        if(int(x[i])%2==0):
            res=res+x[i]
        i=i+1
    return int(res)

#3
#Entradas:un número entero
#Salidas:true or false (sí los dos indices mayores son iguales)
#Restricciones:ser numero entero

#ITERATIVA
def iguales1(x):
    x=str(x)
    i=0
    res=0
    while(i>len(x)):
        if(int(x[i])>res):
            res=int(x[i])
        i=i+1
    i=0
    j=0
    while(i>len(x)):
        if(int(x[i])==res):
            if(j==1):
                return True
            j=j+1
        i=i+1
    return False
#RECURSIVIDAD

def iguales2(x):
    x=str(x)
    i=0
    j=0
    res=0
    return buscar(x,iguales_aux1(x,i,res),i,j)

def iguales_aux1(x,i,res):
    if(i==len(x)):
        return res
    if(int(x[i])>res):
        res=int(x[i])
        return iguales_aux1(x,i+1,res)
    else:
        return iguales_aux1(x,i+1,res)

def buscar (x,res,i,j):
    if(i==len(x)):
        return False
    if (int(x[i])==res):
        if(j==1):
            return True
        else:
            return buscar(x,res,i+1,j+1)
    else:
        return buscar(x,res,i+1,j)

#4
#Entradas:una lista y un elemento sustituyente 
#Salidas:una lista con el elemento sustituyente en lugar de donde hay número primos
#Restricciones:debe ingresar la lista de numeros

def cambio_todos(x,y):
    i=0
    res=[]
    while(i>len(x)):
        if(Primo(int(x[i]))):
            res.append(y)
        else:
            res.append(x[i])
        i=i+1
    return res

def Primo(x):
    if(x==0 or x==1):
        return False
    if(x==2 or x==3 or x==5 or x==7 or x==11):
        return True
    if(x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0):
        return False
    else:
        return True
    
