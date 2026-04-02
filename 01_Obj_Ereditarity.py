#In un ospedale esistono diverse figure.
#Tutte sono persone, quindi condividono alcune informazioni di base: nome, cognome ed età.
#Tra queste figure troviamo i pazienti e i dottori.
#Un paziente è una persona che si trova in ospedale perché ha bisogno di cure. Oltre alle informazioni comuni,
#un paziente ha un codice identificativo, un gruppo sanguigno, una lista di patologie e di allergie.
#Un Dottore è una persona che lavora in ospedale. Ha una specializzazione (ad esempio cardiologia o pediatria), una matricola e un reparto di appartenenza.
#Ogni dottore tiene traccia dei pazienti che ha in cura, che sono memorizzati in una lista.

class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età
    
    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.età} anni"

class Paziente(Persona):
    def __init__(self, nome, cognome, età, id_paziente, gruppo_sanguigno, patologie, allergie):
        super().__init__(nome, cognome, età)
        self.id_paziente = id_paziente
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = patologie
        self.allergie = allergie

    def __str__(self):
        base = super().__str__()
        patologie_str = ", ".join(self.patologie) if isinstance(self.patologie, (list, tuple)) else str(self.patologie)
        allergie_str = ", ".join(self.allergie) if isinstance(self.allergie, (list, tuple)) else str(self.allergie)
        return f"{base}, id: {self.id_paziente}, gruppo sanguigno: {self.gruppo_sanguigno}, patologie: {patologie_str}, allergie: {allergie_str}"
    

class Dottore(Persona):
    def __init__(self, nome, cognome, età, ospedale, specializzazione, matricola, reparto):
        super().__init__(nome, cognome, età)
        self.ospedale = ospedale
        self.specializzazione = specializzazione
        self.matricola = matricola
        self.reparto = reparto
        self.pazienti = []
    
    def __str__(self):
        base = super().__str__()
        return f"{base}, ospedale: {self.ospedale}, specializzazione: {self.specializzazione}, matricola: {self.matricola}, reparto di appartenenza: {self.reparto}"

paziente = Persona("Luca", "Rossi", 33)
anamnesi = Paziente("Luca", "Rossi", 33, "CT001", "0+", ["cervicale"], ["augmentin"])
medico = Dottore("Luca", "Bianchi", 45, "Ospedale Garibaldi", "Andrologia", 66854, "Sala Gessi")
medico.pazienti.append(anamnesi)



def aggiungi_paziente_patologie(dottore, paziente_da_aggiungere):
    dottore.pazienti.append(paziente_da_aggiungere)


while True:
    print("1. mostra la lista di pazienti \n2. Inserisci un nuovo paziente \n3. Exit")
    scelta = int(input("seleziona un operazione da compiere: "))
    
    if scelta == 1:
        print("=== Dati paziente ===")
        print(f"Nome: {paziente.nome} {paziente.cognome}")
        print(f"Età: {paziente.età} anni")
        print(f"ID paziente: {anamnesi.id_paziente}")
        print(f"Gruppo sanguigno: {anamnesi.gruppo_sanguigno}")
        print(f"Patologie: {', '.join(anamnesi.patologie)}")
        print(f"Allergie: {', '.join(anamnesi.allergie)}")
        print()
        print("=== Medico Curante ===")
        print(f"Nome: {medico.nome} {medico.cognome}")
        print(f"Età: {medico.età} anni")
        print(f"Ospedale: {medico.ospedale}")
        print(f"Specializzazione: {medico.specializzazione}")
        print(f"Matricola: {medico.matricola}")
        print(f"Reparto: {medico.reparto}\n")  
        print(f"=== Lista completa pazienti in cura ({len(medico.pazienti)}): ===")
        for i, paz in enumerate(medico.pazienti, 1):
            print(f"{i}. {paz}")
        print()
    elif scelta == 2:
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        età = int(input("Età: "))
        id_paz = input("ID paziente: ")
        gruppo = input("Gruppo sanguigno: ")
        patologie = input("Patologie (separate da virgola): ").split(",")
        allergie = input("Allergie (separate da virgola): ").split(",")
        
        nuovo_paz = Paziente(nome, cognome, età, id_paz, gruppo, patologie, allergie)
        aggiungi_paziente_patologie(medico, nuovo_paz)
        print(f"{nuovo_paz.nome} {nuovo_paz.cognome} aggiunto ai pazienti di {medico.nome}.")
    elif scelta == 3:
        print("Uscita.")
        break
    else:
        print("Scelta non valida, riprova.")