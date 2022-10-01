def agregar(lista,el):
    try:
        if el not in lista:
            lista.append(el)
            print(lista)
        else:
            raise ValueError

    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", [el])

agregar([10, -2, "Hola"], 10)
