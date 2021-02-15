def palindromo():
    print("Escriba el palindromo: ")
    t=input("")
    x=t.replace(" ", "")
    return Aux(x,x,0,0,len(x)-1)



def Aux(x,y,u,temp,temp2):
    
    w=x[temp]
    r=y[temp2]

    print(w,r)
    if(w==r):
        temp+1
        temp2-1
        if(u==len(x)-1):
            return print("si es palindromo")
        else:
            return Aux(x,y,u+1,temp+1,temp2-1)
    else:
        return print("no es palindromo")
palindromo()
