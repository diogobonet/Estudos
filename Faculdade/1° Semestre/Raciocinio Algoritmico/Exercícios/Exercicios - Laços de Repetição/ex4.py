num = int(input("Digite o número para ser decomposto: "))
texto = str(num)
quant = len(texto)

num2 = " "
for i in texto:
  quant1 = quant - 1
  quant = quant1
  if quant1 <= 0:
    num2 += "{}".format(i)
    break

  num2 += "{} x 10^{} + " .format(i, quant1)
print("A decomposição: ", num2)