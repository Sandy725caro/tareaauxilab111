#ejercicio Nro1 
x=3600#hora de tarea
z=1800#tiempo limite
if(z<=x):
    print("justo a tiempo")
else:
    print("no esta dentro del tiempo")
tareaauxilab111


#EJERCICIO Nro 2
a=int(input("ingresar coeficiente de la variable cuadratica"))
b=int(input("ingresar coeficiente de la variable lineal"))
c=int(input("ingresar el termino independiente "))
if((b**2)-4*a*c)<0:
    print("solucion de la ecuacion es con numeros complejos")
else: 
    print("no hay solucion") 
    

#EJERCICIO Nro 3
h=15
m=59
s=59
a=int(input())
s=s+a
if(s>59):
    p=s//60
    s=s%60
    m=m+p
    if(m>59):
        q=m//60
        m=m%60
        h=h+p
        if(h>23):
            t=h//24
            h=h%24
            
print(h,":",m,":",s)
