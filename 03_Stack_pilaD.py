history = ["google.com", "wikipedia.org", "python,org"]
forward = []
current = history.pop() #phyton

print(f"Pagina corrente: {current}")
print(f"Cronologia: {history}")

forward.append(current)
current = history.pop() #wikipedia

print(f"\nPagina corrent: {current}")
print(f"Cronologia: {history}")
print(f"Avanti: {forward}")

history.insert(1,"yahoo.com") #inserisce nel mezzo una pila non lo vede

history[0]
history[1]

print(f"{history}")

history.remove("google.com")
history.pop(0)

print(f"{history}")