from enum import Enum

class TipoContrato(Enum):
    COMI="Comision"
    FIJO="Sueldo Fijo"

class Antiguedad(Enum):
    CAT1= "Menos de 2 anios" #0%
    CAT2= "De 2 a 5 anios"   #5%+
    CAT3= "Mas de 5 anios"   #10%+

class Empleado:
    def __init__(self, DNI, nombre, apellido, anioIng, tipoContrato):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.anioIng = anioIng
        self.tipoContrato = tipoContrato
    def mostrarSalario(self):
        pass

class EmpleadoComision(Empleado):
    def __init__(self, salarioMinimo, clientesCaptados, montoPorCliente):
        super()
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
    def mostrarSalario(self):
        if (self.montoPorCliente*self.clientesCaptados) >= self.salarioMinimo:
            salarioCobrar=self.montoPorCliente*self.clientesCaptados
            return salarioCobrar
        else:
            salarioCobrar=self.salarioMinimo
            return salarioCobrar

class EmpleadoFijo(Empleado):
    def __init__(self, sueldoBasico, Antiguedad):
        super()
        self.sueldoBasico = sueldoBasico
        self.Antiguedad = Antiguedad
    def mostrarSalario(self):
        if self.Antiguedad=="CAT1":
            return self.sueldoBasico
        elif self.Antiguedad=="CAT2":
            return self.sueldoBasico*1.05
        else:
            return self.sueldoBasico*1.10 

emp1 = EmpleadoComision("21222333", "juan","perez",2005,TipoContrato.COMI.value,200000.00,5,1000)
