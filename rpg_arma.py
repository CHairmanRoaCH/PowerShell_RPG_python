import random
import math

class Arma:

    def __init__(self, nombre_arma, danyo_min, danyo_max, probabilidad_fallo, probibilidad_critico:float, multiplicador_critico):#, probabilidad_fallo, probibilidad_critico : int, critico : float):
        self.nombre = nombre_arma
        self.danyo_min = danyo_min
        self.danyo_max = danyo_max
        self.probabilidad_fallo = probabilidad_fallo
        self.probibilidad_critico = probibilidad_critico
        self.multiplicador_critico = multiplicador_critico
        '''
        self.probabilidad_fallo = probabilidad_fallo
        self.probibilidad_critico = probibilidad_critico
        self.critico = critico
        '''

    def danyo_aleatorio(self):
        #danyo_causado = random.randint(self.danyo_min, self.danyo_max)
        #'''
        n = random.random()
        if(n <= self.probabilidad_fallo):
            danyo_causado = 0
        else:
            danyo_causado = random.randint(self.danyo_min, self.danyo_max)
        #'''
        return danyo_causado
    
    def calcular_probabilidad_critico(self, danyo):

        n = random.random()

        if(n <= self.probibilidad_critico):
            
            danyo = danyo * self.multiplicador_critico
            danyo = math.ceil(danyo)
            
        else:
            
            danyo = danyo

        return danyo
        
        

    def __str__(self):
        return f"{self.nombre} | Min:{self.danyo_min}/ Max:{self.danyo_max} Atq\nPorcentaje de fallo: {self.probabilidad_fallo} \nPorcentaje de crítico: {self.probibilidad_critico}\t x{self.multiplicador_critico}"