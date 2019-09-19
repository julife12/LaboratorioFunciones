def a_power_b(a,b):  
    cuadrado=1
    for j in range(1, b+1):
        cuadrado=cuadrado*a

    
    return cuadrado


n1=int(input("digite el primer numero: "))
p1=int(input("digite la potencia: "))
nm1=a_power_b(n1, p1)
print(nm1)
