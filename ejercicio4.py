from collections import deque
#creamos tareas y las ordenamos de manera ascendente

tareas = [[3, "Matemáticas"],[4, "Lengua"], [1, "Química"], [9, "Filosofía"], [2, "Programación"]]
tareas.sort()

#ahora metemos las tareas en una estructura
lista_final = deque(tareas)

#ahora lo que hacemos es que se muestre tan solo el nombre de la tarea y no su duración
for i in range(len(lista_final)):
    print(lista_final[i][1])

#el resultado serían las tareas que debemos de hacer ordenadas de menor a mayor tardanza