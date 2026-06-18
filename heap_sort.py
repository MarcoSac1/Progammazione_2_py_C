import sys
import random
import time

class Persona:
    def __init__(self, nome, eta, ruolo):
        self.nome = nome
        self.eta = eta
        self.ruolo = ruolo

    def __repr__(self):
        return f"{self.nome}({self.eta},{self.ruolo})"

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j].eta <= pivot.eta:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterativo(arr):
    stack = [(0, len(arr) - 1)]
    max_stack_size = 1

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high)
            stack.append((low, p - 1))
            stack.append((p + 1, high))
            max_stack_size = max(max_stack_size, len(stack))

    return arr, max_stack_size

RANGI = [10, 50, 100, 500, 1000, 2000, 3000, 5000, 10000, 50000, 100000]
RUOLI = ["studente", "docente", "bidello", "preside"]

print("=" * 72)
print("  HEAP SORT — Ordinamento iterativo (memoria heap)")
print("=" * 72)
print(f"{'n':>8} | {'tempo (s)':>10} | {'stack_max':>9} | {'heap stack B':>12} | {'esito':>10}")
print("-" * 72)

for n in RANGI:
    random.seed(42)
    originale = [Persona(f"P{i}", random.randint(18, 80), random.choice(RUOLI)) for i in range(n)]

    arr = originale[:]

    start = time.perf_counter()
    ordinato, max_sz = quicksort_iterativo(arr)
    elapsed = time.perf_counter() - start

    heap_bytes = sys.getsizeof(ordinato) + sys.getsizeof(list(range(n)))

    ok = all(ordinato[i].eta <= ordinato[i+1].eta for i in range(len(ordinato)-1))
    esito = "OK" if ok else "ERRORE"

    print(f"{n:>8} | {elapsed:>10.5f} | {max_sz:>9} | {heap_bytes:>12} | {esito:>10}")

print()
print("=" * 72)
print("  COSA SUCCEDE NELL'HEAP")
print("=" * 72)
print("""
  Il 'lavoro rimanente' e' salvato in una lista Python:

    stack = [(0, 9999)]            # tutta la lista da ordinare
    while stack:
        low, high = stack.pop()    # prendo un intervallo
        p = partition(...)          # lo partiziono
        stack.append((low, p-1))   # metto i sotto-intervalli
        stack.append((p+1, high))  # in attesa di processarli

  La lista 'stack' vive nell'HEAP:
    - Cresce e si riduce dinamicamente
    - NON ci sono frame annidati che aspettano
    - Il chiamante NON resta in attesa
    - L'unico frame e' quello di quicksort_iterativo()
""")
print("-" * 72)
print("  DIFFERENZA FONDAMENTALE")
print("-" * 72)
print(f"""
  ┌──────────────────────────┬─────────────────────────────┐
  │   STACK (ricorsione)      │   HEAP (iterativo)          │
  ├──────────────────────────┼─────────────────────────────┤
  │ Ogni chiamata = 1 frame  │ Tutto in una lista           │
  │ Frame annidati = O(n)     │ Nessun annidamento           │
  │ Limite ~1000 frame        │ Solo limiti RAM             │
  │ Ogni frame aspetta i figli│ Elabora e passa oltre       │
  │ Piu' veloce (nativo)      │ Piu' lento (gestione lista) │
  │ RecursionError oltre n    │ Scalabile a n=100000+       │
  └──────────────────────────┴─────────────────────────────┘
""")
