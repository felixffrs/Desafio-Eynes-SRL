"""
Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""
import math

class Circulo():
    def __init__(self, radio):
        if radio > 0:
            self.radio = radio
        else:
            print("Por favor ingrese un radio superior a 0")

    def set_radio(self, radio):
        if radio > 0:
            self.radio = radio
        else:
            print("No esta permitido ingresar un radio inferior a 1")

    def area(self):
        return math.pi * self.radio**2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Radio del circulo: {self.radio}, Area: {self.area()} y el Perimetro: {self.perimetro()}"
    
    def __mul__(self, n):
        if n > 0: 
            new_circle = Circulo(self.radio * n)
            return new_circle
        else:
            print("No esta permitida la multiplicacion con numeros inferiores a 1")
