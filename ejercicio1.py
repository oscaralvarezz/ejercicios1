'''Tenemos que formatear la cadena para posteriormente invertirla'''
from email.headerregistry import ContentTransferEncodingHeader


cadena_nombre = "zeréP nauJ, 01"
cadena_definitiva = cadena_nombre[::-1].split(",")
print(cadena_definitiva[1],"ha sacado un:", cadena_definitiva[0], "de nota")