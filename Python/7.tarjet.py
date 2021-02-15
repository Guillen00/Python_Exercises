#77777
#Entrada:un numeo entero y un digito
#Salida:posibilidades para dar el digito
#Restricciones:ser enteros mayor a 0 

def tarjet(x,y):
   if(x==0):
      print("El digito no puede ser cero")
   else:
      x=str(x)
      return suma(x,0,y)+'   '+multi(x,y,0)
   
def multi(x,y,temp): 
      c=x[temp]
      res=''
      if(int(c)==y):
         if(temp==len(x)-1):
            return res
      if(temp==len(x)-1):
         if(y%int(c)==0):
            res=res+c
         return res
      if(y%int(c)==0):
         res=res+str(c)+'*'
         return res+multi(x,y,temp+1)
      else:
         return multi(x,y,temp+1)


def suma(x,temp,w):
   y=x[temp]
   
   res=str(y)
   
   if(temp==len(x)-1):
      if(int(res)==w):
         return res
      if(int(res)>w):
         temp=0
         return ''
      if(int(res)<w):
         
         return ''
   else:
      if(int(res)==w):
         return ''
      if(int(res)>w):
         temp=0
         return suma(x,temp,w)
      if(int(res)<w):
         return res+'+'+str(suma(x,temp+1,w))   
 
