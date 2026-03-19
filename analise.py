import numpy as np
import matplotlib.pyplot as plt
from disponibilidade import DisponibilidadeServico


class AnaliseDisponibilidade:
    def __init__(self):
        pass

    def calcular_curva(self, n, k, valores_p):
        resultados = []
        for p in valores_p:
            servico = DisponibilidadeServico(n, k, p)
            resultados.append(servico.calcular_disponibilidade())
        return resultados

    def plotar_cenario_1(self):
        """
        Cenário 1:
        n fixo e comparação entre k = 1, k = n/2 e k = n
        """
        n = 10
        valores_p = np.linspace(0, 1, 100)

        valores_k = [1, n // 2, n]

        plt.figure(figsize=(10, 6))

        for k in valores_k:
            disponibilidades = self.calcular_curva(n, k, valores_p)
            plt.plot(valores_p, disponibilidades, label=f"k = {k}", linewidth=3)

        plt.title("Cenário 1: Comparação de k com n = 10")
        plt.xlabel("Probabilidade de cada servidor estar disponível (p)")
        plt.ylabel("Disponibilidade do serviço")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plotar_cenario_2(self):
        """
        Cenário 2:
        k = 1 fixo e comparação entre diferentes valores de n
        """
        valores_n = [2, 5, 10]
        k = 1
        valores_p = np.linspace(0, 1, 100)

        plt.figure(figsize=(10, 6))

        for n in valores_n:
            disponibilidades = self.calcular_curva(n, k, valores_p)
            plt.plot(valores_p, disponibilidades, label=f"n = {n}, k = {k}", linewidth=3)

        plt.title("Cenário 2: Efeito da replicação com k = 1")
        plt.xlabel("Probabilidade de cada servidor estar disponível (p)")
        plt.ylabel("Disponibilidade do serviço")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plotar_cenario_3(self):
        """
        Cenário 3:
        k = n e comparação entre diferentes valores de n
        """
        valores_n = [2, 5, 10]
        valores_p = np.linspace(0, 1, 100)

        plt.figure(figsize=(10, 6))

        for n in valores_n:
            k = n
            disponibilidades = self.calcular_curva(n, k, valores_p)
            plt.plot(valores_p, disponibilidades, label=f"n = {n}, k = {k}", linewidth=3)

        plt.title("Cenário 3: Efeito da replicação com k = n")
        plt.xlabel("Probabilidade de cada servidor estar disponível (p)")
        plt.ylabel("Disponibilidade do serviço")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plotar_cenario_4(self):
        """
        Cenário 4:
        n e p fixos, variando k
        """
        n = 10
        p = 0.8
        valores_k = list(range(1, n + 1))
        disponibilidades = []

        for k in valores_k:
            servico = DisponibilidadeServico(n, k, p)
            disponibilidades.append(servico.calcular_disponibilidade())

        plt.figure(figsize=(10, 6))
        plt.plot(valores_k, disponibilidades, marker="o", linewidth=3)
        plt.title("Cenário 4: Disponibilidade variando k (n = 10, p = 0.8)")
        plt.xlabel("Número mínimo de servidores disponíveis (k)")
        plt.ylabel("Disponibilidade do serviço")
        plt.grid(True)
        plt.show()

    def exibir_menu(self):
        print("\nEscolha o cenário que deseja visualizar:")
        print("1 - Comparar k = 1, k = n/2 e k = n, com n fixo")
        print("2 - Comparar diferentes valores de n com k = 1")
        print("3 - Comparar diferentes valores de n com k = n")
        print("4 - Variar k com n = 10 e p = 0.8")
        print("5 - Exibir todos os cenários")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            self.plotar_cenario_1()
        elif opcao == "2":
            self.plotar_cenario_2()
        elif opcao == "3":
            self.plotar_cenario_3()
        elif opcao == "4":
            self.plotar_cenario_4()
        elif opcao == "5":
            self.plotar_cenario_1()
            self.plotar_cenario_2()
            self.plotar_cenario_3()
            self.plotar_cenario_4()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    analise = AnaliseDisponibilidade()
    analise.exibir_menu()