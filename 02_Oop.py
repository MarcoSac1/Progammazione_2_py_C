class Auto:
    def __init__(self, brand, modello, anno): 
        self.brand = brand
        self.modello = modello  
        self.anno = anno
        self.horsepower = 0  
    
    def descrizione(self):
        return f"la mia auto e' un {self.brand} {self.modello} ({self.anno})" 
    
    def cavalli(self, cv):  
        self.horsepower += cv
        return self.horsepower  

auto1 = Auto("Fiat", "Panda", 1999)
auto2 = Auto("Alfa", "Stelvio", 2024)

print(auto1.descrizione())  
auto1.cavalli(35)
print(f"con {auto1.horsepower} cavalli\n")  

print(auto2.descrizione())  
auto2.cavalli(546)
print(f"con {auto2.horsepower} cavalli")  