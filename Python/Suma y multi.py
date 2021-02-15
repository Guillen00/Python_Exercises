def tarjet(x,y):
   x=str(x)
   return suma(x,0,y)+'   '+multi(x,y,0,'')
   
def multi(x,y,temp,res): 
      c=x[temp]
      if(int(c)==y):
         if(temp==len(x)-1):
            return res
      if(temp==len(x)-1):
         if(y%int(c)==0):
            res=res+c
         return res
      if(y%int(c)==0):
         res=res+str(c)+'*'
         return multi(x,y,temp+1,res)
      else:
         return multi(x,y,temp+1,res)


def suma(x,temp,w):
   y=x[temp]
   val=''
   res=val+str(y)
   
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
 
