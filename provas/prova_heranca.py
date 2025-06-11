# Classe base
class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

# Subclasse Carro
class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

# Subclasse Moto
class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Exemplos de uso
veiculo = Veiculo()
veiculo.movimentar()

carro = Carro()
carro.movimentar()

moto = Moto()
moto.movimentar()
