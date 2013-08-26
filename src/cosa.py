import pilas
pilas.iniciar()
pingu = pilas.actores.Pingu()
contador =  0

def colisionar(actor, enemigo):
    #pilas.avisar("Colision %s %s " % (actor, enemigo))
    if actor.x < enemigo.x:

        enemigo.empujar(100, 10)
    else:
        enemigo.empujar(-100, 10)

    #enemigo.eliminar()

def meter_enemigos():
    # global contador
    # pilas.avisar("El contador vale %d" % contador)
    # contador += 1
    enemigos = pilas.actores.Aceituna() * 3
    enemigos.desordenar()
    enemigos.y = 230
    enemigos.aprender(pilas.habilidades.RebotarComoPelota)
    #enemigos.aprender(pilas.habilidades.PuedeExplotar)
    pilas.escena_actual().colisiones.agregar(pingu, enemigos, colisionar)
    return True

pilas.mundo.agregar_tarea(1, meter_enemigos)
pingu.y = -230

pingu.aprender(pilas.habilidades.SeMantieneEnPantalla)
#pingu.aprender(pilas.habilidades.)
pingu.radio_de_colision = 30
pilas.ejecutar()
