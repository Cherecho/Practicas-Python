# Abecedario
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cifrar(texto,key):
    
    texto_cifrado=""

    for letra in texto:
        
        nueva_posicion=(abecedario.index(letra)+key)
        
        if (nueva_posicion>26):
            nueva_posicion=nueva_posicion-26    
            nueva_posicion=nueva_posicion-1

        letra_cifrada=abecedario[nueva_posicion]
        texto_cifrado+=letra_cifrada

    return texto_cifrado

print("Cifrador césar")

texto_claro=input("Texto a cifrar:")
clave=int(input("Clave de cifrado (un número del 1 al 27):"))


cifrado=cifrar(texto_claro,clave)
print ("Texto cifrado:",cifrado)