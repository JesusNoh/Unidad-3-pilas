class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print(pila.ver_tope())  # Imprime 3
print(pila.desapilar())  # Imprime 3
print(pila.esta_vacia())  # Imprime False