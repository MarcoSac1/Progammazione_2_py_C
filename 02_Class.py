class Persona:
    def __init__(self, nome, eta = 0):
        self.nome = nome
        self._eta = eta
    def get_age(self):
        return self._eta
    def set_age(self, x):
        self._eta = x

class Studente(Persona):
    def __init__(self, nome, _eta, matricola, voto):
        super().__init__(nome, _eta) 
        self.matricola = matricola
        self.voto = voto
    def studia(self):                
        return f"{self.nome} sta studiando."
    def presentati(self):
        return f"ciao sono {self.nome},ho {self._eta} anni, la mia matricola è {self.matricola}, voto medio {self.voto}."

s = Studente("Franco", 32, 4738, 30)
print(s.presentati())
