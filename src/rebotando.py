# encoding: utf-8
import pilas
import random

pilas.iniciar()


pelotas = []
contador_pelotas = 0
texto_contador = pilas.actores.Texto("Pelotas: %d" % contador_pelotas, x=-180, y=230)

class DesapareceSiNoVisible(object):
    '''Elimina actores que no están en pantalla para recuperar memoria'''
    def __init__(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        x = self.receptor.x
        y = self.receptor.y
        ancho = pilas.mundo.motor.ancho_original /2
        alto = pilas.mundo.motor.alto_original /2
        if abs(x) > ancho or abs(y) > alto:
            self.receptor.eliminar()
            self.receptor.destruir()
            pilas.avisar(u"Se quitó una pelota")

    def eliminar(self):
        pass

class Colisionable(object):
    '''Habilidad que da la capacidad a un actor de rebotar objetos'''
    def __init__(self, receptor):
        self.receptor = receptor
        self.figura = pilas.fisica.Rectangulo(0, 0, ancho=receptor.ancho*.75,
                                              alto=receptor.alto*.8, dinamica=False)

    def actualizar(self):
        self.figura.x = self.receptor.x
        self.figura.y = self.receptor.y + 70


dificultad = 4

def crear_pelota():
    '''Teare periódica'''
    global contador_pelotas
    cantidad = random.randint(1, dificultad)
    for i in range(cantidad):
        pelota = pilas.actores.Pelota(300, 100)
        pelota.aprender(DesapareceSiNoVisible)
        empuje_x = random.randrange(-25, -5)
        empuje_y = random.randrange(15, 25)
        #pilas.avisar("Empujando pelota con fuerza %s %s" % (empuje_x, empuje_y))
        pelota.empujar(empuje_x, empuje_y)

    contador_pelotas += cantidad
    texto_contador.texto = "Cantidad: %d" % contador_pelotas
        # Retorna true para seguir en ejecucion
    return True


pingu = pilas.actores.Pingu(y=-240)
pingu.aprender(Colisionable)

pilas.mundo.agregar_tarea(3, crear_pelota)
pilas.escena_actual().fisica.eliminar_paredes()
pilas.ejecutar()
