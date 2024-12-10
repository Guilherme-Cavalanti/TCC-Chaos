import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

class Dimension ():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # Obter limites do espaço do atrator
        self.x_min, self.x_max = np.min(self.x), np.max(self.x)
        self.y_min, self.y_max = np.min(self.y), np.max(self.y)
        self.z_min, self.z_max = np.min(self.z), np.max(self.z)

        self.points = np.array([x, y, z]).T  # Cada linha é um ponto (x, y, z)

        print(f"X min: {self.x_min}   X max: {self.x_max}")
        print(f"Y min: {self.y_min}   Y max: {self.y_max}")
        print(f"Z min: {self.z_min}   Z max: {self.z_max}")

    # Função para contar células ocupadas
    def CountOcuppiedCells(self, points, epsilon):
        # Criar grade: divide cada dimensão pelo tamanho epsilon
        bins_x = np.arange(self.x_min, self.x_max + epsilon, epsilon)
        bins_y = np.arange(self.y_min, self.y_max + epsilon, epsilon)
        bins_z = np.arange(self.z_min, self.z_max + epsilon, epsilon)
        
        # Colocar pontos nas células (índices de cada dimensão)
        indices = np.floor((self.points - np.array([self.x_min, self.y_min, self.z_min])) / epsilon).astype(int)
        
        # Criar conjunto único de células ocupadas
        occupied_cells = set(map(tuple, indices))
        return len(occupied_cells)

    epsilons = []
    cell_counts = []
    def BoxCounting(self):
        # Definir tamanhos de célula (epsilon) em uma escala logarítmica
        self.epsilons = np.logspace(-1.3, 1.3, num=100)  # Exemplo: de 10^-2 a 10^0 (ajuste conforme o atrator)
        print(f"epsilons: {self.epsilons}")

        # Contar o número de células ocupadas para cada epsilon
        self.cell_counts = [self.CountOcuppiedCells(self.points, epsilon) for epsilon in self.epsilons]
        print(f"cell counts: {self.cell_counts}")

    fractal_dimension = 0
    def CalculateFractalDimension(self):

        self.BoxCounting()

        # 5. Ajustar reta log-log
        log_eps = np.log(1 / self.epsilons)  # log(1/epsilon)
        log_counts = np.log(self.cell_counts)  # log(N(epsilon))

        # Regressão linear para calcular a inclinação (dimensão fractal)
        slope, intercept, r_value, p_value, std_err = linregress(log_eps, log_counts)

        # 6. A dimensão fractal é a inclinação da reta
        self.fractal_dimension = round(slope,2)
        print(f"Dimensão Fractal: {self.fractal_dimension}")
        plt.loglog(self.epsilons, self.cell_counts, marker='o', linestyle='-', color='b')
        plt.show()