from attractor import Attractor
from dimension import Dimension

# Parâmetros a,b,c necessários
params = [0.2, 0.2, 9.2]

# Condições iniciais com e sem o erro
initial_state = [1.0, 1.0, 1.0]
x_error = 1+10**-10
initial_state_e = [x_error,1.0,1.0]

##Testando atrator
Atrator = Attractor(params,initial_state)
#AtratorErro = Attractor(params, initial_state_e)
#Atrator.PlotVar("z")
#Atrator.ComparePlot("y",AtratorErro)
#Atrator.PlotAttractor()
Atrator.PoincareMap()

#### Calcular Dimensão Fractal ####
# Dimensoes = Dimension(x,y,z)
# Dimensoes.CalculateFractalDimension()