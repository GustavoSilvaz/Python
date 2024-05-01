largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura * altura
tinta = area / 2

print("A área da parede é de {}x{} Sua área é de {}m²".format(largura,altura,area))
print("Para pintar esta parede você precisará de {:.4f}L de tinha".format(tinta))