class Stack:
    def __init__(self):# Inizializza una pila vuota.
        self.__items = []

    def is_empty(self):# Verifica se la pila è vuota.
        return len(self.__items) == 0

    def push(self, __item):# Aggiunge un elemento in cima alla pila.
        self.__items.append(__item)

    def pop(self):# Rimuove e restituisce l'elemento in cima. Solleva un errore se vuota.
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("pop da una pila vuota")

    def peek(self):# Restituisce l'elemento in cima senza rimuoverlo.
        if not self.is_empty():
            return self.__items[-1]
        return None

    def size(self):# Restituisce il numero di elementi nella pila.
        return len(self.__items)

    def insert(self, index, item):
        self.__items.insert(index, item)

    def __str__(self):# Permette di stampare la pila.
        return str(self.__items)


pila = Stack()
pila.push('Google.com')     #0 A
pila.push('Wikipedia.com') # B
pila.push('python.org')     # C

print(f"Pila attuale: {pila}")      # Output: ['A', 'B', 'C']
print(f"Elemento in cima (peek): {pila.peek()}") # Output: C
print(f"Pop: {pila.pop()}")         # Output: C
print(f"Pila dopo pop: {pila}")     # Output: ['A', 'B']
print(f"Dimensione: {pila.size()}") # Output: 2

pila.insert(1, 'proton.me') 
pila.insert(2, 'facebook.com') #tre elementi al centro della pila
pila.insert(3, 'wireshark.org')

print(f"Pila dopo l'insert: {pila}") #stampo la pila
print(f"Dimensione dopo l'insert: {pila.size()}") # Output: 5
