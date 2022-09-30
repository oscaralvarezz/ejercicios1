'''Realiza un programa que cumpla el siguiente algoritmo
utilizando siempre que sea posible operadores en asignación:'''

numero_magico = 123456789
numero_usuario = int(input("Escribe un número entre 1 y 9:"))
 
#realizamos al función
def multiplication(numero_usuario):
    numero_usuario *= 9
    numero_usuario *= numero_magico
    return numero_usuario

print(multiplication(numero_usuario))
    