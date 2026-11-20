class Conjuro:
    def __init__(self, nombre_conjuro, tipo_conjuro, efecto_conjuro, magia_necesaria):
        self.nombre_conjuro = nombre_conjuro
        self.tipo_conjuro = tipo_conjuro
        self.efecto_conjuro = efecto_conjuro
        self.magia_necesaria = magia_necesaria

    def __str__(self):
        return f"{self.nombre_conjuro} | {self.magia_necesaria} PM | {self.efecto_conjuro} {self.tipo_conjuro}"

    