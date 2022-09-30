'''Realiza una función separar(lista) que tome una lista
de números enteros y devuelva dos listas ordenadas.
La primera con los números pares y la segunda con los números impares.'''

impares = []
pares= []

def separar(lista):
    for numero in range(len(lista)):
        if lista[numero]%2==0:
            valores_pares = lista[numero]
            pares.append(valores_pares)
        else:
            valores_impares = lista[numero]
            impares.append(valores_impares)

separar([1,3,8,2,4,13,53,6,9,12])
print("Los numeros impares son:", impares)
print("Los numeros pares son", pares)
