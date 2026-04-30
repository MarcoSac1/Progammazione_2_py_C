class Stack:
    
    def __init__(self):
        self.item = [] #inizializo una pila vuota

    def is_empty(self): #verifica se la pila e vuota
        return len(self.items) == 0
    
    def push(self, item): #aggiunge un elemento in cima alla pila.
        self.item.append(item)
    
    def pop(self): # rimuve e restituisce l'elemento in cima solleva un errore se vuota    
        if not self.is_empty():
            return self.items.pop()
        raise IndexError(f"pop da una pila vuota")
    
    def peek(self): #permette di stampare la pila
        return str(self.item)
        
# --- Esempio di Utilizzo ---
pila = Stack()
pila.push('A')
pila.push('B')
pila.push('C')

print(f"Pila attuale: {pila}")      # Output: ['A', 'B', 'C']
print(f"Elemento in cima (peek): {pila.peek()}") # Output: C
print(f"Pop: {pila.pop()}")         # Output: C
print(f"Pila dopo pop: {pila}")     # Output: ['A', 'B']
print(f"Dimensione: {pila.size()}") # Output: 2


