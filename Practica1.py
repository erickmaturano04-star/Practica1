"""
Titulo: Estructura de Arbol Binario
Autor: Edilson Mamani
Fecha: 17/03/2026
"""
class Nodo:
    """Representa un nodo individual en el arbol binario
        Atributos:
            _dato (int): El valor numerico almacenado en el nodo
            _izq (Nodo): Referencia al hijo izquierdo (menores)
            _der (Nodo): Referencia al hijo derecho (mayores)
    """
    def __init__(self, dato):
        """Inicializa un nodo con un valor especifico
            Argumento:
                dato (int): El valor se guardara en este nodo
        """
        self._dato = dato
        self._izq = None
        self._der = None
    
    def __str__(self):
        """Devuelve una representación en cadena del dato"""
        return str(self._dato)
    
    #Getter y Setter para 'dato'
    @property
    def dato(self):
        """Obtiene el valor del nodo"""
        return self._dato
    
    @dato.setter
    def dato(self, valor):
        """Asigna un nuevo valor al nodo"""
        self._dato = valor
        
    #Getter y Setter para 'izq'
    @property
    def izq(self):
        """Obtiene el nodo hijo izquierdo"""
        return self._izq
    
    @izq.setter
    def izq(self, nodo):
        """Asigna un nodo como hijo izquierdo"""
        self._izq = nodo
        
    #Getter y Setter para 'der'
    @property
    def der(self):
        """Obtiene el nodo hijo derecho"""
        return self._der
    
    @der.setter
    def der(self, nodo):
        """Asigna un nodo como hijo derecho"""
        self._der = nodo
        
        
class Arbol:
    """Clase principal del Arbol Binario
        Atributos:
            _raiz (Nodo): El nodo principal que sirve como entrada al Arbol
    """
    def __init__(self):
        """Inicializa un Arbol Vacio"""
        self._raiz = None
        
    #Getter y Setter para 'raiz'
    @property
    def raiz(self):
        """Devuelve la raíz del árbol para lectura"""
        return self._raiz
    
    @raiz.setter
    def raiz(self, nodo):
        """Permite modificar la raiz del Arbol"""
        self._raiz = nodo
        
    def insertar(self, dato):
        """Inserta un nuevo valor en el Arbol
            Argumento:
                dato (int): El numero entero que se desea agregar
        """
        self._raiz = self._insertar(dato, self._raiz)
    
    def _insertar(self, dato, nodo_actual):
        """Logica interna recursiva para agregar datos al Arbol
            Argumento:
                dato (int): Valor a insertar
                nodo_actual (Nodo): Nodo en el que se encuentra la recursion
            Retorna:
                Nodo: EL nodo (nuevo o existente) para reconstruir los enlaces
        """
        #Caso Base: Si el nodo esta vacio, crea el nodo
        if nodo_actual is None:
            return Nodo(dato)
        #Logica del Arbol(izquierda 'menores', derecha 'mayores')
        if dato < nodo_actual.dato:
            nodo_actual.izq = self._insertar(dato, nodo_actual.izq)
        elif dato > nodo_actual.dato:
            nodo_actual.der = self._insertar(dato, nodo_actual.der)
        return nodo_actual
        
        
def main():
    """Punto de entrada principal del programa
        Aqui se realizan las pruebas de la estructura
    """
    a1 = Arbol()
    a1.insertar(40)
    a1.insertar(20)
    a1.insertar(60)
    print("La raiz es:", a1.raiz.dato)
    print("El hijo izq es:", a1.raiz.izq)
    print("El hijo der es:", a1.raiz.der)

if __name__ == "__main__":
    """ Este bloque asegura que el codigo solo se ejecute si este
        archivo se abre directamente y no si se importa desde otro lugar
    """
    main()