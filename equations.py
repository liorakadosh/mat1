def exp (x:float, y:float):
    y=int(y)
    num=1
    for i in range (0,y):
        num=num*x
    return(num)

def factorial (x:float):
    num=1
    y=int(x)+1
    for i in range (1,y):
        num=num*i
    return(num)
        
def exponent (x:float):
    num_total=0
    for i in range(0,100):
        num1=exp(x,i)
        num2=factorial(i)
        num_total=num_total+(num1/num2)
    return(num_total)

def Ln (x:float):
    num=0
    if x<=0:
        return(0.0)
    for i in range(0,100):
        num=num+2*((x-exponent(num))/(x+exponent(num)))   
    return(num)
    
def XtimesY (x:float, y:float):
    if (x!=0) and (y==0):
        return(1)
    if x<=0:
        return(0.0)

    num=exponent(y*Ln(x))
    if (x<0) and (y%2!=0):
        return(-num)
    else:
        return(num)
    
def sqrt (x:float, y:float):
    x=1/x
    num=XtimesY(y, x)
    return(num)
   
def calculate (x:float):
    if x==0:
        return(0.0)
    num=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    num=float('%0.6f'% num)
    return(num)

