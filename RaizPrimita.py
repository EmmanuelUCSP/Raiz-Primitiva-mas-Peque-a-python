# Python encontrar raiz primitiva
from math import sqrt
 
# Verifica si n es primo
def EsPrimo( n):
    if (n <= 1): return False
    if (n <= 3): return True
    if (n % 2 == 0 or n % 3 == 0): return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True
 
# Calcula (x^n)%p
def power( x, y, p):
    res = 1 #Variable que almacena el resultado
    x = x % p # actualizamos x si x<= p
 
    while (y > 0):
        if (y & 1): res = (res * x) % p # Si y es impar, multiplicamos x por el resultado
        y = y >> 1 
        x = (x * x) % p

    return res
 

# Encuentras los factores de un numero
def findPrimefactors(s, n) :
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
 
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :    # Mientras divido n, imprima iy divida n 
            s.add(i)
            n = n // i
         
    if (n > 2) : s.add(n) # si un numero primo es mayor a 2
 

# Encuentra la raiz primitiva mas pequeña haciendo uso de las demas funciones
def findPrimitive( n) :
    s = set()
  
    if (EsPrimo(n) == False): return -1 #Verificacion del primo
    phi = n - 1
 
    findPrimefactors(s, phi) #Encuentra los factores primos de phi and store in a set
 
    for r in range(2, phi + 1): # revisa cada numero desde 2 hasta phi
        flag = False

        for it in s:
            if (power(r, phi // it, n) == 1): #si es que mod n es 1
                flag = True
                break
        if (flag == False): return r
 
    return -1 # Si no se encontro una raiz primitiva
 

#Codigo Principal
n = int(input("Ingresa un número: "))
print("La raiz primitiva mas pequeña de",n, "es", findPrimitive(n))