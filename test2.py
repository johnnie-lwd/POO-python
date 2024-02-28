# declaré y definí mi función
def sumar_iva(precioInicial):
    precioConIva = precioInicial * 1.21
    return precioConIva       

# ALGORITMO
# 1. entrada de datos
# 2. procesamiento de datos - cuerpo de la función
# 3. el retorno de datos

# ejecutarla 
print(sumar_iva(4500))
print(sumar_iva(12600))
print(sumar_iva(3900))

def saludar(nombre, apellido, curso):
    saludo = f'Hola {nombre} {apellido}! '
    bienvenida= f'Bienvenido al curso de {curso}'
    return saludo + bienvenida

print(saludar("Pepe", "Martinez", "Python"))
print(saludar("Tito", "Rodriguez", "Java"))