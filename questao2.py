tempo_banho = int(input("quanto tempo de banho? "))
litros_minutos = 9
gasto_no_banho = tempo_banho * litros_minutos
qtda_banhos = 1000 / gasto_no_banho
print("para um banho de %d minutos, 1m3 permite %d banhos." % (tempo_banho, qtda_banhos))
