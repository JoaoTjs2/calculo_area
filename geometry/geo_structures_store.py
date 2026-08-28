class GeoStructure:
    def calc_area(self):
        raise

class Retangle(GeoStructure):
    def __init__(self, dim1: float, dim2: float):
        self.dim1 = dim1
        self.dim2 = dim2

    def calc_area(self) -> float:
        return self.dim1 * self.dim2

class Triangle(GeoStructure):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calc_area(self) -> float:
        return (self.base * self.altura)/2

class Trapezy(GeoStructure):
    def __init__(self, b_maior: float, b_menor: float, altura: float):
        self.b_maior = b_maior
        self.b_menor = b_menor
        self.altura = altura

    def calc_area(self):
        return ((self.b_maior + self.b_menor) * self.altura)/2