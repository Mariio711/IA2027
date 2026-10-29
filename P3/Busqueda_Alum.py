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
            nuevoEstado = aplicaOperador(op, nodo.estado)
            hijo = Nodo(nuevoEstado, op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
            sucesores.append(hijo)
    return sucesores

def BFS() -> None:
    objetivo = False

    raiz = NodoInicial()
    abiertos = []
    sucesores = []
    cerrados = []
    abiertos.append(raiz)
    contador = 0

    while abiertos and not objetivo:
        actual = abiertos[0]
        abiertos.pop(0)
        cerrados.append(actual)
        objetivo = testObjetivo(actual.estado)
        if not objetivo:
            sucesores = expandir(actual)
            abiertos.extend(sucesores)
            contador += 1

    if objetivo:
        dispSolucion(actual)
        print("solucion encontrada en ", contador)
    elif not objetivo:
        print("No se ha encontrado solución")

def DFS() -> None: #es un copia pega de BFS hay que cambiar cosas aun
    objetivo = False
    
    raiz = NodoInicial()
    abiertos = []
    sucesores = []
    cerrados = []
    abiertos.append(raiz)
    contador = 0

    while abiertos and not objetivo:
        actual = abiertos[0]
        abiertos.pop(0)
        cerrados.append(actual)
        objetivo = testObjetivo(actual.estado)
        if not objetivo:
            sucesores = expandir(actual)
            abiertos.extend(sucesores)
            contador += 1

    if objetivo:
        dispSolucion(actual)
        print("solucion encontrada en ", contador)
    elif not objetivo:
        print("No se ha encontrado solución")



