class Auto:
    # propiedades /atributos
    def __init__(self, marca, modelo, color, anio) -> None:
        self.marca= marca
        self.modelo=modelo
        self.color= color
        self.anio=anio

    #metodos / comportamientos, acciones
        
    #getter 
    def getMarca(self):
        return self.marca 
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAnio(self):
        return self.anio
       
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()} ')
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')  
        print(f'Anio: {self.getAnio()}')

     # setters y getters - metosos
     # setter - establecer valores de cada atributo4
     # getter -    
auto1=Auto("toyota","prius","rojo","2020")
auto2=Auto("ford","mustang","azul","1965")

auto1.mostrarAuto()
auto2.mostrarAuto()
