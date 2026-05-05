class NodoD:
    def __init__(self, valore):
        self.valore = valore
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda = None
        self.__size = 0

    def insertFirst(self, valore):
        nuovo = NodoD(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda = nuovo
            nuovo.next = nuovo
            nuovo.prev = nuovo
        else:
            nuovo.next = self.__testa
            nuovo.prev = self.__coda
            self.__testa.prev = nuovo
            self.__coda.next = nuovo
            self.__testa = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = NodoD(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda = nuovo
            nuovo.next = nuovo
            nuovo.prev = nuovo
        else:
            nuovo.prev = self.__coda
            nuovo.next = self.__testa
            self.__coda.next = nuovo
            self.__testa.prev = nuovo
            self.__coda = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")

        corrente = self.__testa
        for _ in range(self.__size):
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo = NodoD(nuovo_valore)
                nuovo.next = corrente.next
                nuovo.prev = corrente
                corrente.next.prev = nuovo
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next

        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")

        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return

        corrente = self.__testa
        for _ in range(self.__size):
            if corrente.valore == valore_riferimento:
                nuovo = NodoD(nuovo_valore)
                nuovo.next = corrente
                nuovo.prev = corrente.prev
                corrente.prev.next = nuovo
                corrente.prev = nuovo
                self.__size += 1
                return
            corrente = corrente.next

        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")

        valore = self.__testa.valore

        if self.__size == 1:
            self.__testa = None
            self.__coda = None
        else:
            self.__testa = self.__testa.next
            self.__testa.prev = self.__coda
            self.__coda.next = self.__testa

        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")

        valore = self.__coda.valore

        if self.__size == 1:
            self.__testa = None
            self.__coda = None
        else:
            self.__coda = self.__coda.prev
            self.__coda.next = self.__testa
            self.__testa.prev = self.__coda

        self.__size -= 1
        return valore

    def removeValue(self, valore):
        if self.isEmpty():
            raise ValueError("lista vuota")

        if self.__testa.valore == valore:
            return self.removeFirst()

        corrente = self.__testa.next
        for _ in range(self.__size - 1):
            if corrente.valore == valore:
                if corrente == self.__coda:
                    return self.removeLast()
                corrente.prev.next = corrente.next
                corrente.next.prev = corrente.prev
                self.__size -= 1
                return valore
            corrente = corrente.next

        raise ValueError(f"{valore} non trovato nella lista")

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def peekLast(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__coda.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        if self.isEmpty():
            return "CircularLinkedList([])"

        elementi = []
        corrente = self.__testa
        for _ in range(self.__size):
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "CircularLinkedList([" + " ⟷ ".join(elementi) + "])"

    def traverse(self, n):
        if self.isEmpty():
            return []

        elementi = []
        corrente = self.__testa
        for _ in range(n):
            elementi.append(corrente.valore)
            corrente = corrente.next
        return elementi


cl = CircularLinkedList()

# 1) Aggiungi in ordine: "alice", "bob", "carlo"
cl.insertLast("alice")
cl.insertLast("bob")
cl.insertLast("carlo")

# 2) Stampa la lista
print("Lista iniziale:", cl,"\n")

# 3) Simula 6 turni con traverse(6)
print("6 turni:", cl.traverse(6),"\n")

# 4) Aggiungi "diana" dopo "bob"
cl.insertAfter("bob", "diana,\n")

# 5) Stampa la lista aggiornata
print("Lista aggiornata:", cl,"\n")

# 6) Simula altri 8 turni
print("8 turni:", cl.traverse(8),"\n")

# 7) "bob" lascia il team
cl.removeValue("bob")

# 8) Stampa la lista aggiornata
print("Lista dopo la rimozione di bob:", cl ,"\n")

# 9) Simula altri 6 turni
print("6 turni senza bob:", cl.traverse(6),"\n")

# 10) Stampa quanti analisti sono nel team
print("Numero analisti:", cl.size())

