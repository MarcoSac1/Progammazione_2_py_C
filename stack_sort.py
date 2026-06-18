import sys
import random
import time

sys.setrecursionlimit(10**6)

class Persona:
    def __init__(self, nome, eta, ruolo):
        self.nome = nome
        self.eta = eta
        self.ruolo = ruolo

    def __repr__(self):
        return f"{self.nome}({self.eta},{self.ruolo})"

depth_stats = {"max": 0, "current": 0, "calls": 0}

def quicksort_recursive(arr):
    depth_stats["calls"] += 1
    depth_stats["current"] += 1
    depth_stats["max"] = max(depth_stats["max"], depth_stats["current"])

    if len(arr) <= 1:
        depth_stats["current"] -= 1
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x.eta <= pivot.eta]
    right = [x for x in arr[:-1] if x.eta > pivot.eta]

    result = quicksort_recursive(left) + [pivot] + quicksort_recursive(right)

    depth_stats["current"] -= 1
    return result

RANGI = [10, 50, 100, 500, 1000, 2000, 3000, 5000]

print("=" * 72)
print("  STACK SORT — Ordinamento ricorsivo (call stack)")
print("=" * 72)
print(f"{'n':>8} | {'tempo (s)':>10} | {'prof. max':>9} | {'chiamate':>9} | {'esito':>10}")
print("-" * 72)

RUOLI = ["studente", "docente", "bidello", "preside"]

for n in RANGI:
    random.seed(42)
    originale = [Persona(f"P{i}", random.randint(18, 80), random.choice(RUOLI)) for i in range(n)]

    depth_stats = {"max": 0, "current": 0, "calls": 0}
    arr = originale[:]

    start = time.perf_counter()
    try:
        ordinato = quicksort_recursive(arr)
        elapsed = time.perf_counter() - start
        ok = all(ordinato[i].eta <= ordinato[i+1].eta for i in range(len(ordinato)-1))
        esito = "OK" if ok else "ERRORE"
        print(f"{n:>8} | {elapsed:>10.5f} | {depth_stats['max']:>9} | {depth_stats['calls']:>9} | {esito:>10}")
    except RecursionError:
        elapsed = time.perf_counter() - start
        print(f"{n:>8} | {elapsed:>10.5f} | {'-':>9} | {'-':>9} | {'RECURSION':>10}")
        print(f"\n  -> RECURSION ERROR a n={n}: lo stack delle chiamate e' esaurito!")
        print(f"  -> Default recursion limit: 1000 frame")
        print(f"  -> Con array grandi, la ricorsione supera il limite")
        break

print()
print("=" * 72)
print("  COSA SUCCEDE NELLO STACK (call stack)")
print("=" * 72)
print("""
  Quando chiami quicksort_recursive(arr):

    main:
      ├── chiama quicksort_recursive(arr)  -> frame #0
      │   ├── chiama quicksort_recursive(left) -> frame #1
      │   │   ├── quicksort_recursive(left2)    -> frame #2
      │   │   │   ...
      │   │   │   └── ritorna (frame rimosso)
      │   │   └── quicksort_recursive(right2)   -> frame #2
      │   │       ...
      │   └── quicksort_recursive(right)     -> frame #1
      │       ...

  Nel caso peggiore (array gia' ordinato), la profondita' = n
  Con n=5000 servono 5000 frame annidati -> RecursionError!

  OGNI frame occupa memoria nello stack:
    - parametri (arr, pivot, left, right)
    - indirizzo di ritorno
    - variabili locali
""")
print("-" * 72)
print("  COLLEGAMENTO SICUREZZA:")
print("""
  In C, uno stack overflow puo' sovrascrivere l'indirizzo di
  ritorno (return address) -> buffer overflow -> esecuzione
  di codice arbitrario. Python lo previene con RecursionError.
""")
