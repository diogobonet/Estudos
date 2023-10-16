largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
área = largura * altura 
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²!" .format(largura, altura, área))
calculo2 = área / 2
print("Você precisará gastar exatamente {}l de tinta para pintar essa parede!" .format(calculo2))