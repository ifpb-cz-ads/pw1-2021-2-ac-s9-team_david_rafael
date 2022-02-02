class Televisao():
    def __init__(self, min, max):
        self.tamanho = 0
        self.marca = ""
        self.canal = min
        self.cMinino = min
        self.cMaximo = max


    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cMinino:
            self.canal -= 1
        else:
            self.canal = self.cMaximo

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cMaximo:
            self.canal += 1
        else:
            self.canal = self.cMinino
