inferior = superior = medio = 0

for i in range(10):
    altura = float(input('Digite sua altura: '))

    if altura < 1.6:
        inferior += 1
    elif altura > 1.8:
        superior += 1
    else:
        medio += 1
    
total = inferior + superior + medio

print('-*-' * 15)
print('Pessoas com altura menor que 1.60 ------> {}' .format(inferior))
print('Pessoas com altura maior que 1.80 ------> {}' .format(superior))
print('Pessoas com altura entre 1.60 e 1.80 ---> {}' .format(medio))
print('Total de pessoas cadastradas -----------> {}' .format(total))
print('-*-' * 15)
