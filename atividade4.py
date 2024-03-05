# Objeto pai, Aimal
class Animal():

# Inicializa atributos porte cor idade e tamanho
    def __init__(self, porte, cor, idade, tamanho):
        self.porte = porte
        self.cor = cor;
        self.idade = idade;
        self.tamanho = tamanho;

# Herda classe Animal
class Cachorro(Animal):       
    
    def fazerSom(self):
        print("Au au")

# Herda classe Animal
class Gato(Animal):
    
    def fazerSom(self):
        print("Miau Miau")

# Inicia instancia do objeto gato
gato = Gato('Medio', 'Preto', 12, 60)