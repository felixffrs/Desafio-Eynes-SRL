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
        """
        Test constructor circulo
        >>> circle = Circulo(0)
        Traceback (most recent call last):
        ...
        ValueError: Por favor ingrese un radio superior a 0
        >>> circle = Circulo(-1)
        Traceback (most recent call last):
        ...
        ValueError: Por favor ingrese un radio superior a 0
        """
        if radio > 0:
            self.radio = radio
        else:
            raise ValueError("Por favor ingrese un radio superior a 0")

    def set_radio(self, radio):
        """
        Test constructor circulo
        >>> circle = Circulo(5)
        >>> circle.set_radio(0)
        Traceback (most recent call last):
        ...
        ValueError: No esta setear un radio con un valor inferior a 1
        >>> circle = Circulo(6)
        >>> circle.set_radio(-1)
        Traceback (most recent call last):
        ...
        ValueError: No esta setear un radio con un valor inferior a 1
        """
        if radio > 0:
            self.radio = radio
        else:
            raise ValueError("No esta setear un radio con un valor inferior a 1")

    def area(self):
        """
        Test area circulo
        >>> circle = Circulo(1) 
        >>> circle.area()
        3.141592653589793
        >>> circle = Circulo(3)
        >>> circle.area()
        28.274333882308138
        """
        return math.pi * self.radio**2
    
    def perimetro(self):
        """
        Test perimetro circulo
        >>> circle = Circulo(1) 
        >>> circle.perimetro()
        6.283185307179586
        >>> circle = Circulo(3)
        >>> circle.perimetro()
        18.84955592153876
        """
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Radio del circulo: {self.radio}, Area: {self.area()} y el Perimetro: {self.perimetro()}"
    
    def __mul__(self, n):
        """
        Test multiplicacion
        >>> circle = Circulo(1)
        >>> circle.area()
        3.141592653589793
        >>> new_circle = circle * 3
        >>> new_circle.area()
        28.274333882308138
        """
        if n > 0: 
            new_circle = Circulo(self.radio * n)
            return new_circle
        else:
            print("No esta permitida la multiplicacion con numeros inferiores a 1")

if __name__ == "__main__":
    import doctest
    doctest.testmod()