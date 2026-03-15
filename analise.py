import numpy as np
import matplotlib.pyplot as plt
from disponibilidade import DisponibilidadeServico

class AnaliseDisponibilidade:
    def __init__(self, n):
        self.n = n

    def gerar_valores(self, k, valores_p):
        resultados = []
        for p in valores_p:
            servico = DisponibilidadeServico(self.n, k, p)
            resultados.append(servico.calcular_disponibilidade())
        return resultados

    def plotar_grafico(self):
        valores_p = np.linspace(0, 1, 100)

        k1 = 1
        k2 = self.n // 2
        k3 = self.n

        disp_k1 = self.gerar_valores(k1, valores_p)
        disp_k2 = self.gerar_valores(k2, valores_p)
        disp_k3 = self.gerar_valores(k3, valores_p)

        plt.figure(figsize=(10, 6))
        plt.plot(valores_p, disp_k1, label=f"k = {k1}", linewidth=3)
        plt.plot(valores_p, disp_k2, label=f"k = {k2}", linewidth=3)
        plt.plot(valores_p, disp_k3, label=f"k = {k3}", linewidth=3)

        plt.title(f"Disponibilidade do serviço replicado (n = {self.n})")
        plt.xlabel("Probabilidade de cada servidor estar disponível (p)")
        plt.ylabel("Disponibilidade do serviço")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    n = int(input("Digite o número total de servidores (n): "))
    analise = AnaliseDisponibilidade(n)
    analise.plotar_grafico()