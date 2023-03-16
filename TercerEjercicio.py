numeros = []
multiplosDeDos = []
multiplosDeTres = []
multiplosDeAmbos = []

for i in range(0, 3):
    numeros.append(int(input("Digite un numero entero: ")))
    
for numero in numeros:
    if numero % 2 == 0 and numero % 3 == 0:
        multiplosDeDos.append(numero)
        multiplosDeTres.append(numero)
        multiplosDeAmbos.append(numero)
        continue
    else:
        if numero % 2 == 0:
            multiplosDeDos.append(numero)
        elif numero % 3 == 0:
            multiplosDeTres.append(numero)
        
print(f'Son multiplos de dos {len(multiplosDeDos)} numeros')
print(f'Son multiplos de tres {len(multiplosDeTres)} numeros')
print(f'Son multiplos de ambos {len(multiplosDeAmbos)} numeros')