from math import comb

class DisponibilidadeServico:
    def __init__(self, n, k, p):
        self.n = n
        self.k = k
        self.p = p
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.n, int) or self.n <= 0:
            raise ValueError("n deve ser um inteiro maior que 0.")

        if not isinstance(self.k, int) or self.k <= 0 or self.k > self.n:
            raise ValueError("k deve ser um inteiro tal que 0 < k <= n.")

        if not isinstance(self.p, (int, float)) or not (0 <= self.p <= 1):
            raise ValueError("p deve ser um número entre 0 e 1.")

    def calcular_disponibilidade(self):
        disponibilidade = 0

        for i in range(self.k, self.n + 1):
            termo = comb(self.n, i) * (self.p ** i) * ((1 - self.p) ** (self.n - i))
            disponibilidade += termo

        return disponibilidade


if __name__ == "__main__":
    try:
        n = int(input("Digite o número total de servidores (n): "))
        k = int(input("Digite o número mínimo de servidores disponíveis (k): "))
        p = float(input("Digite a probabilidade de cada servidor estar disponível (p): "))

        servico = DisponibilidadeServico(n, k, p)
        resultado = servico.calcular_disponibilidade()

        print(f"Disponibilidade do serviço: {resultado * 100:.2f}%")

    except ValueError as e:
        print(f"\nErro: {e}")