# crea una classe base Persona con nome, cognome, età
# una classe Dottore con specializzazione e stipendio
# e un paziente con attributo gruppo sanguigno e una lista di patologie

class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.età} anni"


class Dottore(Persona):
    def __init__(self, nome, cognome, età, specializzazione, stipendio):
        super().__init__(nome, cognome, età)
        self.specializzazione = specializzazione
        self.stipendio = stipendio

    def __str__(self):
        base = super().__str__()
        return f"{base}, specializzazione: {self.specializzazione}, stipendio: {self.stipendio}"


class Paziente(Persona):
    def __init__(self, nome, cognome, età, gruppo_sanguigno, patologie):
        super().__init__(nome, cognome, età)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = patologie

    def __str__(self):
        base = super().__str__()
        patologie_str = ", ".join(self.patologie)
        return f"{base}, gruppo sanguigno: {self.gruppo_sanguigno}, patologie: {patologie_str}"


utente = Persona("Franco", "Tarantino", 49)
print(f"Il paziente è: {utente}")

medico = Dottore("Luca", "Bianchi", 45, "Andrologia", 66854)
print(f"Il medico curante è: {medico}")

patologie = ["Prostatite"]
paziente = Paziente("Franco", "Tarantino", 49, "0+", patologie)

print(f"Le patologie del paziente {utente}  sono: {patologie[0]}, riconosciute dal medico specializato in: {medico.specializzazione}")
