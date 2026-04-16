from abc import ABC, abstractmethod


class Veicolo(ABC):
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    @abstractmethod
    def descrivi(self):
        pass


class Auto(Veicolo):
    def __init__(self, marca, modello, anno):
        super().__init__(marca, modello, anno)
        self._velocita = 0

    def accelera(self):
        self._velocita += 10
        print(f"{self.marca} {self.modello} accelera a {self._velocita} km/h")

    def frena(self):
        if self._velocita >= 10:
            self._velocita -= 10
        print(f"{self.marca} {self.modello} frena a {self._velocita} km/h")

    def descrivi(self):
        print(f"Auto: {self.marca} {self.modello} ({self.anno}), velocità: {self._velocita} km/h")

    def get_velocita(self):
        return self._velocita

    def set_velocita(self, nuova_velocita):
        if 0 <= nuova_velocita <= 400:
            self._velocita = nuova_velocita
            print(f"Velocità impostata a {self._velocita} km/h \n")
        else:
            print("Errore: Velocità non valida (0-400 km/h)")


auto_base = Auto("Fiat", "Panda", 2022)

auto_base.accelera()
auto_base.accelera()
auto_base.set_velocita(150)
auto_base.descrivi()


class AutoElettrica(Auto):
    def __init__(self, marca, modello, anno, autonomia):
        super().__init__(marca, modello, anno)
        self.autonomia = autonomia
        self._percentuale_batteria = 100

    def mostra_autonomia(self):
        print(f"La {self.marca} {self.modello} ha un'autonomia di {self.autonomia} km")

    def accelera(self):
        if self._percentuale_batteria > 0:
            self._percentuale_batteria -= 2
            self._velocita += 10
            print(f"{self.marca} {self.modello} accelera a {self._velocita} km/h con batteria al {self._percentuale_batteria}%")
        else:
            print(f"{self.marca} {self.modello} non può accelerare: batteria scarica")


auto_elettrica = AutoElettrica("Tesla", "Model X Plaid", 2025, 760)
auto_elettrica.set_velocita(320)
auto_elettrica.descrivi()
auto_elettrica.mostra_autonomia()
auto_elettrica._percentuale_batteria = 36
auto_elettrica.accelera()