# libreria necesaria para simular aleatoridad
import random
from art_contraneitor import logo

# caracteres que se usaran en la generación de contraseñas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(logo)
print('¡Bienvenido a Contraneitor!')

# pregunta al usuario los datos necesarios para le generación de la contraseña
num_letras = int(input('¿Cuántas letras deben estar en su contraseña? '))
num_numeros = int(input('¿Cuántos números deben estar en su contraseña? '))
num_simbolos = int(input('¿Cuántos símbolos deben estar en su contraseña? '))

contraseña = []

for i in range(num_letras):
    letra = random.choice(letras)
    contraseña.append(letra)
for i in range(num_numeros):
    numero = random.choice(numeros)
    contraseña.append(numero)
for i in range(num_simbolos):
    simbolo = random.choice(simbolos)
    contraseña.append(simbolo)

# como la lista se creó siguiendo el orden letras -> numeros -> simbolos, se revuelven los carácteres para hacer más difícil los intentos de adivinar la contraseña
random.shuffle(contraseña)

# ahora, la lista pasa a apuntar a un string
contraseña = ''.join(contraseña)

# finalmente, se imprime la contraseña
print(f'Su contraseña es: {contraseña}')