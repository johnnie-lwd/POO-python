num1=5
num2=7
opc=input("ingrese opcion (A-B):")
def funcion(opcion):
    if opcion == "A":
        print(num1*num2)
    elif opcion=="B":
        print(num1-num2)
funcion(opc)    