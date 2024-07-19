# print("Hello")
# print("nice to meet you: " + input("Cual es tu nombre(s): ") + " " 
#       + input("cual es tu apellido(s): "))
# edad = input("cual es tu edad:")
# print(edad)
# edad1 = int(edad)
# print(type(edad1))
# num = input("escribe un numero: ")
# num2 = int(num)
# mul = num2 * 2
# print(mul)
# adi1 = num2 + 5
# sus1 = num2 - 8
# pro1 = num2 * 5
# div1 = num2 / 3
# print(f"el resultado dela suma es: {adi1}\n el resultado de la resta es: {sus1}\n el resultado del producto es: {pro1}\n el resultado de la division es {div1}")

print("hello") 
nombre = input("escribe tu nombre completo: ") #dando valor a la variable nombre desde la entrada de la consola
edad = input("cual es tu edad: ") #dando valor a la variable edad desde la entrada de la consola
print(f"nice to meet you {nombre} and happy that have reached your {edad} years that have many more with health,life,abundance and wisdom ")
                                    #un print con forma dando un orden de impresion concatena
                                    #  bariables y cadenas de strings sin ningun operador.
numero = input("escrive un numero:")
num1 = int(numero) #cambiando de string a un valor numerico entero a la variable "numero" y su nuevo
                    #su nuevo valor queda almacenado en "num1"
print(type(num1))   #para observar el tipo de la variable ya se int,flot,string
res_pro = num1 * 2  #operacion de multiplicacion ya que "num1"tiene balor int que lo combierte del valor
                    #ingresado por consola a la variable numero
print(res_pro)
edad1 = int(edad)
print(type(edad1))
print("con el numero que introdugiste aremos las operaciones basicas de aritmetica")
adicion = edad1 + num1  #se realiza oreraciones entre variables ya que tienen valore
sustrac = edad1 - num1  #numericos int y se almacena en otra variable
product = edad1 * num1
divicio = edad1 / num1
print(f" suma {adicion}\n resta {sustrac}\n multiplicacion {product}\n division {divicio}")
#a qui nueba mente un print con forma de impresion y salto de linea de las variales 
#de las operaciones anterires 