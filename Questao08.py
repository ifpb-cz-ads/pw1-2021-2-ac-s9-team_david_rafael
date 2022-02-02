class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def população(self):
        return sum([c.população for c in self.cidades])


class Cidade:
    def __init__(self, nome, população):
        self.nome = nome
        self.população = população
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"


am = Estado("Ceara", "CE")
am.adiciona_cidade(Cidade("Lavras da Mangabeira", 31476))
am.adiciona_cidade(Cidade("Juazeiro do norte", 278264))
am.adiciona_cidade(Cidade("Crato", 133031))

sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 11376685))
sp.adiciona_cidade(Cidade("Guarulhos", 1244518))
sp.adiciona_cidade(Cidade("Campinas", 1098630))

rj = Estado("Paraiba", "PB")
rj.adiciona_cidade(Cidade("Cajazeiras", 62576))
rj.adiciona_cidade(Cidade("João Pessoa", 825796))
rj.adiciona_cidade(Cidade("Souza", 69997))


for estado in [ce, sp, pb]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")