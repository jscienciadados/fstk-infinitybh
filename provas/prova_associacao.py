class ContaBancaria:
    """
    Representa uma conta bancária com saldo e titular.
    Os atributos _saldo e _titular são protegidos por convenção,
    e o acesso é controlado por métodos públicos.
    """
    def __init__(self, titular, saldo_inicial=0.0):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): O nome do titular da conta.
            saldo_inicial (float): O saldo inicial da conta (padrão é 0.0).
                                   Deve ser um valor não negativo.
        """
        if not isinstance(titular, str) or len(titular.strip()) == 0:
            raise ValueError("O titular deve ser uma string não vazia.")
        if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
            raise ValueError("O saldo inicial deve ser um número não negativo.")

        self._titular = titular  # Atributo protegido por convenção
        self._saldo = float(saldo_inicial) # Atributo protegido por convenção

    def depositar(self, valor):
        """
        Deposita um valor na conta.

        Args:
            valor (float): O valor a ser depositado. Deve ser positivo.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O valor do depósito deve ser um número positivo.")
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        self.exibir_saldo()

    def sacar(self, valor):
        """
        Saca um valor da conta, se houver saldo suficiente.

        Args:
            valor (float): O valor a ser sacado. Deve ser positivo.

        Returns:
            bool: True se o saque foi bem-sucedido, False caso contrário.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O valor do saque deve ser um número positivo.")
        if valor > self._saldo:
            print(f"Saldo insuficiente. Saldo atual: R${self._saldo:.2f}. Valor solicitado: R${valor:.2f}.")
            return False
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            self.exibir_saldo()
            return True

    def exibir_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo:.2f}")

    # Método para obter o titular (getter para o atributo _titular)
    def get_titular(self):
        """
        Retorna o nome do titular da conta.
        """
        return self._titular

    # Exemplo de como não expor o saldo diretamente, mas permitindo leitura
    # Você pode criar um getter para o saldo se precisar acessá-lo sem modificá-lo
    # def get_saldo(self):
    #     return self._saldo

# --- Demonstração de Uso ---
print("--- Testando a Classe ContaBancaria ---")

# Criando uma conta bancária
try:
    minha_conta = ContaBancaria("João Silva", 1000.00)
    minha_conta.exibir_saldo()
except ValueError as e:
    print(f"Erro ao criar conta: {e}")
    minha_conta = None # Para evitar erros se a conta não for criada

if minha_conta:
    # Realizando depósitos
    minha_conta.depositar(250.75)
    minha_conta.depositar(50.00)

    # Tentando sacar
    minha_conta.sacar(300.00)
    minha_conta.sacar(1500.00) # Tentando sacar mais do que o saldo

    # Exibindo saldo novamente
    minha_conta.exibir_saldo()

    # Acessando o titular via getter
    print(f"\nTitular da conta: {minha_conta.get_titular()}")

    # Exemplos de entrada inválida
    print("\n--- Testando entradas inválidas ---")
    try:
        ContaBancaria("", 500)
    except ValueError as e:
        print(f"Erro esperado: {e}")

    try:
        ContaBancaria("Ana", -100)
    except ValueError as e:
        print(f"Erro esperado: {e}")

    try:
        minha_conta.depositar(-100)
    except ValueError as e:
        print(f"Erro esperado: {e}")

    try:
        minha_conta.sacar(0)
    except ValueError as e:
        print(f"Erro esperado: {e}")