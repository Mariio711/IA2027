import numpy as np

from dataclasses import dataclass


@dataclass
class tEstado:
    t: np.ndarray
    N: int
    fila: int
    col: int

    def __init__(self, tablero: np.ndarray) -> None:
        self.t = tablero
        filas, cols = np.where(tablero == 0) # Devuelve dos listas (filas y columnas donde está el 0)
        self.fila = filas.item() # Sólo queremos el valor y como es único, .item() o [0]
        self.col = cols.item()
        self.N = tablero.shape[0]


operadores = {"8": "ARRIBA", "2": "ABAJO", "4": "IZQDA", "6": "DRCHA"}
    
def estadoInicial() -> tEstado:
    puzle_inicial = np.array([
        [1, 2, 3],
        [8, 4, 0],
        [7, 6, 5]
    ])
    return tEstado(puzle_inicial)
    # return tEstado(np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])) # Pruebe esta combinación tras haber comprobado la anterior

def estadoObjetivo() -> tEstado:
    puzle_final = np.array([
        [1, 2, 3],
        [0, 4, 5],
        [8, 7, 6]
    ])
    return tEstado(puzle_final)
    # return tEstado(np.array([[1, 3, 0], [8, 2, 4], [7, 6, 5]])) #Pruebe esta combinación tras haber comprobado la anterior

def aplicaOperador(op: int, estado: tEstado) -> tEstado:
    nuevo = tEstado(estado.t.copy()) # Nuevo objeto, copia del anterior

    # Completado ✔️
    match operadores[op]:
        case "ARRIBA":
            nuevo.t[estado.fila, estado.col] = estado.t[estado.fila - 1, estado.col]
            nuevo.t[estado.fila - 1, estado.col] = 0
            nuevo.fila = estado.fila - 1
        case "ABAJO":
            nuevo.t[estado.fila, estado.col] = estado.t[estado.fila + 1, estado.col]
            nuevo.t[estado.fila + 1, estado.col] = 0
            nuevo.fila = estado.fila + 1
        case "IZQDA":
            nuevo.t[estado.fila, estado.col] = estado.t[estado.fila, estado.col - 1]
            nuevo.t[estado.fila, estado.col - 1] = 0            
            nuevo.col = estado.col - 1
        case "DRCHA":
            nuevo.t[estado.fila, estado.col] = estado.t[estado.fila, estado.col + 1]
            nuevo.t[estado.fila, estado.col + 1] = 0
            nuevo.col = estado.col + 1
    return nuevo


def esValido(op: int, estado: tEstado) -> bool:
    valido = False
    # Completado ✔️
    match operadores[op]:
        case "ARRIBA":
            valido = (estado.fila > 0)
        case "ABAJO":
            valido = (estado.fila < (estado.N - 1))
        case "IZQDA":
            valido = (estado.col > 0)
        case "DRCHA":
            valido = (estado.col < (estado.N - 1))
    return valido

def iguales(estado: tEstado, objetivo: tEstado) -> bool:
    return np.array_equal(estado.t, objetivo.t)
    
    
def testObjetivo(estado: tEstado) -> bool:
    objetivo = False
    objetivo = iguales(estado, estadoObjetivo())
    return objetivo


def coste(operador: str, estado: tEstado) -> int:
    return 1
