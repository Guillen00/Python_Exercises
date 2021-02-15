#Recursion en pila vs recursion en cola

#Entrada: Una lista
#S La suma de los numeros pares de la lista
#Restricciones: No puede ser una lista vacia

#RECURSION EN PILA
def sumaPares_Pila(lista):
    if(len(lista) == 0):
        print("La lista esta vacia")
    else:
        return sumarPares_aux(lista,0)

def sumarPares_aux(lista,i):
    res = 0
    if(i == len(lista) - 1):
        if(lista[i]%2 == 0):
            res = res + lista[i]
        return res
       
    if(lista[i]%2 == 0):
        res = res + lista[i]
        return res + sumarPares_aux(lista, i+1)
    else:
        return res + sumarPares_aux(lista, i+1)

#RECURSION EN COLA
def sumaPares_Cola(lista):
    if(len(lista) == 0):
        print("La lista esta vacia")
    else:
        return sumarCola_aux(lista,0,0)

def sumarCola_aux(lista,i,res):
    if(i == len(lista) - 1):
        if(lista[i]%2 == 0):
            res = res + lista[i]
        return res
           
    if(lista[i]%2 == 0):
        res = res + lista[i]
        return sumarCola_aux(lista, i+1, res)
    else:
        return sumarCola_aux(lista, i+1, res)
