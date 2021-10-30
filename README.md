#Codigo hecho en Python
primero se importa "sqrt" de la libreria math

definimos distintas funciones para poder tener un codigo mas ordenado

#Primero definimos una funcion para saber si el numero
#ingresado es primo

	si n<=1 no es primo, si n<=3 es primo
	hacemos uso de un while que comprara el residuo de la
	division entre "n" e "i" que aumentara progresivamente

#Despues definimos la funcion Power

	la funcion power se usa para el calculo de (x^n)%p
	inicializando el resultado "res" como 1
	haciendo uso de un while(y>0)
		que si "y" es impar multiplicamos x por el resultado

#Se define la funcion FindPrimefactors

	la funcion se usa para almacenar los factores primos
	de un numero
	
	con un while añadimos el numero de 2 que divide a n
	luego haciendo uso de un for que va desde 3 hasta la raiz de n
		dentro un while que verifica si "i" divine a "n"

	por ultimo si n>2 agregamos n 


#La funcion que recopila todas estas la llamamos findPrimitive
	inicializamos un set() para guardar los valore que obtendremos en FindPrimefactors
	
	#Llamamos a la funcion para verificar si es primo
		si no es primo retornamos -1

	inicializamos phi = n-1 y llamamos a findPrimefactors(s, phi)
	luego usamos un for para revisar los numeros desde 2 hasta phi
		Repetimos todos los factores primos de phi y verificamos si 
		encontramos una potencia con valor 1 	
	
		Comprobamos si r^((phi)/prime factors) mod n es 1

	Si no hubiera potencia con valor 1 solo retornamos -1

#Finalmente en "la funcion main" pedimos 1 numero al usuario
#y ejecutamos findPrimitive imprimiendolo





	
  