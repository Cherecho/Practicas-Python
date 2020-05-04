# Abecedario
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Cifrador césar")

texto_claro=input("Texto a cifrar:")
clave=int(input("Clave de cifrado (un número del 1 al 27):"))


texto_cifrado=""

for letra in texto_claro:
    nueva_posicion=(abecedario.index(letra)+clave) % 27
    letra_cifrada=abecedario[nueva_posicion]
    texto_cifrado+=letra_cifrada

print(texto_cifrado)