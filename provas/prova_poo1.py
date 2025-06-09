class Animal:
    def falar(self):
        """
        Método que imprime um som genérico de animal.
        """
        print("Este animal faz um som genérico.")

class Cachorro:
    def falar(self):
        """
        Método que imprime o som de um cachorro.
        """
        print("O cachorro está latindo.")

class Gato:
    def falar(self):
        """
        Método que imprime o som de um gato.
        """
        print("O gato está miando.")

# Criando um objeto da classe Animal
meu_animal = Animal()

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro()

# Criando um objeto da classe Gato
meu_gato = Gato()

# Chamando o método falar() de cada objeto
print("--- Sons dos Animais ---")
meu_animal.falar()
meu_cachorro.falar()
meu_gato.falar()
print("-----------------------")