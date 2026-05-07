import ipaddress
import random
from collections import deque
from time import perf_counter

# converte IP stringa -> intero
def ipToInt(ip):
    return int(ipaddress.ip_address(ip))

# converte intero -> IP stringa
def intToIp(n):
    return str(ipaddress.ip_address(n))


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.sinistra = None
        self.destra = None


class BST:
    def __init__(self):
        self.radice = None

    def inserisci(self, valore):
        if self.radice is None:
            self.radice = Nodo(valore)
            return

        corrente = self.radice
        while True:
            if valore < corrente.valore:
                if corrente.sinistra is None:
                    corrente.sinistra = Nodo(valore)
                    return
                corrente = corrente.sinistra
            elif valore > corrente.valore:
                if corrente.destra is None:
                    corrente.destra = Nodo(valore)
                    return
                corrente = corrente.destra
            else:
                return

    def cerca(self, valore):
        corrente = self.radice
        while corrente:
            if valore == corrente.valore:
                return True
            if valore < corrente.valore:
                corrente = corrente.sinistra
            else:
                corrente = corrente.destra
        return False


def genera_ip():
    return f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"


# 1) genero 1000 IP casuali per la blacklist
blacklist_ip = list({genera_ip() for _ in range(2000)})[:1000]
blacklist_int = [ipToInt(ip) for ip in blacklist_ip]

# li inserisco nel BST
albero = BST()
for ip in blacklist_int:
    albero.inserisci(ip)

# 2) prendo 10 IP dalla blacklist
ip_bloccati = random.sample(blacklist_ip, 10)

# 3) genero 10 IP nuovi mai visti
ip_nuovi = []
while len(ip_nuovi) < 10:
    ip = genera_ip()
    if ip not in blacklist_ip and ip not in ip_nuovi:
        ip_nuovi.append(ip)

# 4) creo i 20 pacchetti
pacchetti = []

for ip in ip_bloccati + ip_nuovi:
    pacchetti.append({
        "ip_sorgente": ip,
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": random.randint(64, 1500)
    })

random.shuffle(pacchetti)
coda = deque(pacchetti)

# 5) processo i pacchetti
bloccati = 0
permessi = 0

while coda:
    pacchetto = coda.popleft()
    ip = pacchetto["ip_sorgente"]

    if albero.cerca(ipToInt(ip)):
        print(ip, "-> BLOCCATO")
        bloccati += 1
    else:
        print(ip, "-> PERMESSO")
        permessi += 1

# 6) riepilogo finale
print("\nBloccati:", bloccati)
print("Permessi:", permessi)

# 7) confronto tempi BST e lista
ip_test = ip_bloccati + ip_nuovi

inizio = perf_counter()
for ip in ip_test:
    albero.cerca(ipToInt(ip))
tempo_bst = perf_counter() - inizio

inizio = perf_counter()
for ip in ip_test:
    ipToInt(ip) in blacklist_int
tempo_lista = perf_counter() - inizio

print(f"\nTempo BST: {tempo_bst:.8f} s")
print(f"Tempo lista: {tempo_lista:.8f} s")

if tempo_bst < tempo_lista:
    print(f"Il BST è circa {tempo_lista / tempo_bst:.2f} volte più veloce della lista")
else:
    print(f"La lista è circa {tempo_bst / tempo_lista:.2f} volte più veloce del BST")