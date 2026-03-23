import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from disponibilidade import DisponibilidadeServico


class SimuladorEstocastico:

    def __init__(self, rodadas=1000000):
        self.rodadas = rodadas

    def simular(self, n, k, p):
        sucessos = 0

        for _ in range(self.rodadas):
            servidores = np.random.rand(n)
            ativos = np.sum(servidores <= p)

            if ativos >= k:
                sucessos += 1

        return sucessos / self.rodadas

def comparar(n, k):
    simulador = SimuladorEstocastico()
    valores_p = np.linspace(0.1, 0.9, 9)

    resultados = []

    for p in valores_p:
        analitico = DisponibilidadeServico(n, k, p).calcular_disponibilidade()
        experimental = simulador.simular(n, k, p)

        resultados.append({
            "p": p,
            "Analítico": analitico,
            "Experimental": experimental,
            "Erro": abs(analitico - experimental)
        })

    df = pd.DataFrame(resultados)
    print("\nTabela de comparação:\n")
    print(df.to_string(index=False))

    return df


def plotar(df, n, k):
    plt.figure(figsize=(10, 6))

    plt.plot(df["p"], df["Analítico"], label="Analítico", marker='o')
    plt.plot(df["p"], df["Experimental"], label="Experimental", marker='x')

    plt.title(f"Simulação vs Teoria (n={n}, k={k})")
    plt.xlabel("Probabilidade p")
    plt.ylabel("Disponibilidade")

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    n = 10
    k = 6

    df = comparar(n, k)
    plotar(df, n, k)