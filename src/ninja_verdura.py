import pilas
pilas.iniciar()

class PantallaBienvenida(pilas.escena.Normal):
    def __init__(self):
        pilas.escena.Normal.__init__(self)
    def iniciar(self):
        pilas.fondos.Pasto()
        texto = pilas.actores.Texto("Bienvenido a pilas!!!")


