#invertir numero

#libreeria
import math


print("                    ")
print("   invertir numero  ")
print("                    ")

#input
n = input("Digite un numero de 4 digitos: ")
n = int(n)

#processing

r4 = n%10
r3 = (n//10)%10
r2 = (n//100)%10
r1 = (n//1000)%10

ni = r4*1000 + r3*100 + r2*10 + r1

#output
print("Resultado")
print("Numero original: " + str(n))
print("Ultimo digito: " + str(r4))
print("Tercer digito: " + str(r3))
print("Segundo digito " + str(r2))
print("Primer digito: " + str(r1))
print("El numero invertido es: " + str(ni))
