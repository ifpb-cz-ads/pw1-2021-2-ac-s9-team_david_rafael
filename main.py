from Televisao import Televisao


#Questao 1
tv1 = Televisao(2, 10)
tv1.tamanho = 10
tv1.marca = "teste1"

tv2 = Televisao()
tv2.tamanho = 5
tv2.marca = "teste2"

print("A tv tem {} Polegadas e eh de {} marca".format(tv1.tamanho,tv1.marca))
print("A tv tem {} Polegadas e eh de {} marca".format(tv2.tamanho, tv2.marca))


#Questao 2
print(tv1.canal)
tv1.canal = 3
print(tv1.canal)

#Questao 3
tv1.muda_canal_para_baixo()
print(tv1.canal)
tv1.muda_canal_para_baixo()
print(tv1.canal)
tv1.muda_canal_para_baixo()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)

