#55555555555
#Entradas:dos numero
#Salidas:el resultado de la funcion de anckermann con los valores ingresados
#Restricciones:sea entero

def Ackermann(m,n):
    if(m==int(m)):
            
        if(n==int(n)):          
            if(m==0):
                return n+1
            if(m>0 and n==0):
                return Ackermann(m-1,1)
            if(m>0 and n>0):
                return Ackermann(m-1,Ackermann(m,n-1))
        else:
            return print("Error el segundo argumento debe ser un numero natural")
    else:
        return print("Error el primer argumento debe ser un numero natural")
