from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        return self.__data[0]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue({list(self.__data)})"


coda = Queue()
coda.enqueue("Mario")
coda.enqueue("Giulia")
coda.enqueue("Tonino")
coda.enqueue("Rosa")

print(coda)
print("Servo:", coda.peek(),"\n")
print("Persone ancora in fila:", coda.size()-1) 
coda.dequeue()
print(coda)


print("Persone ancora in fila:", coda.size()-1,"\n")
coda.enqueue("Enzo")
print(coda)

while not coda.isEmpty():
    print("Servo:", coda.peek())
    print("Persone ancora in fila:", coda.size()-1)
    coda.dequeue()
    print("Rimangono:", coda, "\n")

print("Coda vuota")