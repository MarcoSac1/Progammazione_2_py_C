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
        if 0 <= nuova_velocita <= 200:  # Limiti realistici
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