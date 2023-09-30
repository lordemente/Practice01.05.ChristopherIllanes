
número_de_payasos = int(input("Número de payasos vendidos"))
número_de_muñecas = int(input("Número de muñecas vendidas"))
peso_Payaso = 112 / 1000
peso_muñeca = 75 / 1000

Juguetes_vendidos = (número_de_payasos + número_de_muñecas)
print("juguetes vendidos", Juguetes_vendidos)


Peso_total = (número_de_payasos * peso_Payaso) + (número_de_muñecas * peso_muñeca)

print("Payasos vendidos", número_de_payasos)
print("Muñecas vendidas", número_de_muñecas)

print("peso de la caja", Peso_total, "kg")

