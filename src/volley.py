
import pilas
ANCHO, ALTO = 640, 480
pilas.iniciar(ancho=ANCHO, alto=ALTO, titulo="Volley")



pilas.fondos.Pasto()
personaje_1 = pilas.actores.Pingu()
personaje_1.x = -(ANCHO / 4) - personaje_1.ancho / 2
personaje_1.y = -(ALTO / 2)

personaje_2 = pilas.actores.Pingu()
personaje_2.espejado = True
personaje_2.x = ANCHO / 4 + personaje_2.ancho / 2
personaje_2.y = -(ALTO/2)
print personaje_2.habilidades

pelota = pilas.actores.Pelota()
pelota.x = personaje_1.x
pelota.y = personaje_1.y + 100

pilas.ejecutar()