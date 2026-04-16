class Auto:
    def __init__(self, marca, modello, anno):
        self.marca = marca        # Pubblico (accessibile direttamente)
        self.modello = modello    # Pubblico
        self.anno = anno          # Pubblico
        self._velocita = 0        # Privato (convenzione Python con _)

    def accelera(self):
        self._velocita += 10
        print(f"{self.marca} {self.modello} accelera a {self._velocita} km/h")

    def frena(self):
        if self._velocita >= 10:
            self._velocita -= 10
        print(f"{self.marca} {self.modello} frena a {self._velocita} km/h")

    def descrivi(self):
        print(f"Auto: {self.marca} {self.modello} ({self.anno}), velocità: {self._velocita} km/h")

    # Getter per accedere alla velocità in modo controllato
    def get_velocita(self):
        return self._velocita

    # Setter con validazione
    def set_velocita(self, nuova_velocita):
        if 0 <= nuova_velocita <= 400:  # Limiti realistici
            self._velocita = nuova_velocita
            print(f"Velocità impostata a {self._velocita} km/h")
        else:
            print("Errore: Velocità non valida (0-200 km/h)")

mia_auto = Auto("Fiat", "Panda", 2022)

mia_auto.accelera()     
mia_auto.accelera()      
print(mia_auto.get_velocita())  
mia_auto.set_velocita(150)  
mia_auto.descrivi()

class AutoEletrica(Auto):
    def __init__(self, marca, modello, anno,autonomia):
        super().__init__(marca, modello, anno)
        self.autonomia = autonomia
        
    def range(self):
        print(f"La {self.marca} ha un autonomia di {self.autonomia} km")
        
    def descrivi(self):
        return super().descrivi()
        
mia_auto = AutoEletrica ("Tesla", "Model X Plaid", 2025, 760 )
mia_auto.range()
mia_auto.set_velocita(320)
mia_auto.descrivi()