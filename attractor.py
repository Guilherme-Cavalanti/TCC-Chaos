import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Attractor ():
    #Inicializa classe com parâmetros e estado inicial
    def __init__(self, params, initial_state):
        self.params = params
        self.initial_state = initial_state
        self.a = self.params[0]
        self.b = self.params[1]
        self.c = self.params[2]
        self.ResolveSystem()

    #Intervalos de tempo
    t_span = (0, 400)  # Intervalo de tempo
    t_eval = np.linspace(*t_span, 10000)  # Pontos de tempo para avaliação
    # Definir as equações de Rössler
    @staticmethod
    def rossler(t, state, a, b, c):
        x, y, z = state
        dxdt = -y - z
        dydt = x + a * y
        dzdt = b + z * (x - c)
        return [dxdt, dydt, dzdt]
    x = []
    y = []
    z = []
    t = []
    
    # Resolver o sistema de equações diferenciais
    def ResolveSystem(self):
        solution = solve_ivp(self.rossler, self.t_span, self.initial_state, args=(self.a, self.b, self.c), t_eval=self.t_eval)
        self.x, self.y, self.z = solution.y
        self.t = solution.t 
    
    #Plotar a variação de uma variável no tmepo
    def PlotVar(self, var):
        #Verificar qual das 3 variáveis é
        if var == "x":
            plt.plot(self.t,self.x, label="Normal") 
            plt.xlabel('x')
            plt.ylabel('t')
            plt.title('Variação de x')
            plt.show()
        elif var == "y":
            plt.plot(self.t,self.y, label="Normal") 
            plt.xlabel('y')
            plt.ylabel('t')
            plt.title('Variação de y')
            plt.show()
        elif var == "z":
            plt.plot(self.t,self.z, label="Normal") 
            plt.xlabel('z')
            plt.ylabel('t')
            plt.title('Variação de z')
            plt.show()
    
    #Comparar a variação em 2 atratores com estados iniciais diferentes
    def ComparePlot(self, var, atrator2):
        if var == "x":
            plt.plot(self.t,self.x, label="Normal") 
            plt.plot(atrator2.t,atrator2.x, label="Erro") 
            plt.xlabel('x')
            plt.ylabel('t')
            plt.legend()
            plt.title('Variação de x')
            plt.show()
        elif var == "y":
            plt.plot(self.t,self.y, label="Normal") 
            plt.plot(atrator2.t,atrator2.y, label="Erro") 
            plt.xlabel('y')
            plt.ylabel('t')
            plt.legend()
            plt.title('Variação de y')
            plt.show()
        elif var == "z":
            plt.plot(self.t,self.z, label="Normal") 
            plt.plot(atrator2.t,atrator2.z, label="Erro") 
            plt.xlabel('z')
            plt.ylabel('t')
            plt.legend()
            plt.title('Variação de z')
            plt.show()
    
    #Gerar o gráfico do atrator
    def PlotAttractor(self):        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(self.x, self.y, self.z)
        plt.title('Atrator de Rossler')
        plt.show()

    #SEÇÃO DE POINCARE
    def PoincareMap(self):
        y_plane = 0.1
        crossing_points_x = []
        crossing_points_z = []

        for i in range(1, len(self.y)):
            # Detecta cruzamento de z[i-1] para z[i] pelo valor fixado
            if (self.y[i-1] < y_plane and self.y[i] >= y_plane):  # Cruzando o plano y
                # Interpolação linear para encontrar x e y no cruzamento exato
                alpha = (y_plane - self.y[i-1]) / (self.y[i] - self.y[i-1])
                x_cross = self.x[i-1] + alpha * (self.x[i] - self.x[i-1])
                z_cross = self.z[i-1] + alpha * (self.z[i] - self.z[i-1])
                
                # Armazena os pontos de cruzamento
                crossing_points_x.append(x_cross)
                crossing_points_z.append(z_cross)

        #Plot da seção de Poincaré
        plt.figure(figsize=(8, 6))
        plt.plot(crossing_points_x, crossing_points_z, 'o', markersize=2, color='blue')
        plt.title(f'Seção de Poincaré para o Atrator de Rössler no plano y={y_plane}')
        plt.xlabel('x')
        plt.ylabel('z')
        plt.grid(True)
        plt.show()
    
        


    

    