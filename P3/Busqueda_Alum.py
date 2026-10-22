from __future__ import annotations
from dataclasses import dataclass
from NPuzle_Alum import tEstado, esValido, aplicaOperador, estadoInicial, testObjetivo, operadores, coste


@dataclass
class Nodo:
    estado: tEstado
    operador: str 
    costeCamino: int 
    profundidad: int
    padre: Nodo 

def NodoInicial() -> Nodo:
    return Nodo(estadoInicial(), "", 0, 0, None)   

def dispCamino(nodo: Nodo) -> None:
    camino = []
    aux = nodo

    while aux is not None:
        camino.append(aux)
        aux = aux.padre
        
    camino.reverse()
    
    print("Estado inicial:\n", camino[0].estado.t, "\n")
    
    for n in camino[1:]:
        op = operadores[n.operador]
        print(f"Movimiento hacia: {op}\n{n.estado.t}\n")


def dispSolucion(nodo: Nodo):
    dispCamino(nodo)
    print("Profundidad: ", nodo.profundidad)
    print("Coste: ", nodo.costeCamino)

def expandir(nodo: Nodo) -> list:
    sucesores = []
    for op in operadores:
        if esValido(op, nodo.estado):
            nuevo: Nodo
            nuevo.estado = aplicaOperador(op, nodo.estado) #aqui me quede

    return sucesores

def BFS() -> None:
    objetivo = False

    raiz = NodoInicial()
    abiertos = []
    sucesores = []
    cerrados = []
    abiertos.append(raiz)

    # Completar el resto del código

    if objetivo:
        dispSolucion()  # Completar
    elif not objetivo:
        print("No se ha encontrado solución")

# Implementar la búsqueda en profundidad
    
    
    