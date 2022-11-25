dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram rodados com o carro alugado? "))

valorCobrado = (dias * 60) + (0.15 * km)

print(f"O aluguel de {dias} dias com {km} rodados\nficou no valor de R${valorCobrado}.")

