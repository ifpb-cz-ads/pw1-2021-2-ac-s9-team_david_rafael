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

#Questão 5

tv3 = Televisao(1, 10)
tv3.tamanho = 32
tv3.marca = "Sansung"

print("A televisao tem {} polegadas e eh a marcar {} e atualmente esta no canal {}".format(tv3.tamanho, tv3.marca, tv3.canal))

tv4 = Televisao(1, 10)
tv4.tamanho = 50
tv4.marca = "Positivo"

print("A televisao tem {} polegadas e eh a marcar {} e atualmente esta no canal {}".format(tv4.tamanho, tv4.marca, tv4.canal))
tv4.muda_canal_para_baixo()
print("O canal foi alterado {}".format(tv4.canal))
tv4.muda_canal_para_baixo()
print("O canal foi alterado para {}".format(tv4.canal))
