from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return elemento in self.elementos

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro):
        for elemento in otro.elementos:
            if not self.contiene(elemento):
                self.elementos.append(elemento)

    def __add__(self, otro):
        resultado = Conjunto(f"{self.nombre} UNIDO {otro.nombre}")
        resultado.unir(self)
        resultado.unir(otro)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        resultado = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if elemento in conjunto2.elementos:
                resultado.agregar_elemento(elemento)
        return resultado

    def __str__(self):
        elementos_str = ', '.join(str(elemento.nombre) for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"