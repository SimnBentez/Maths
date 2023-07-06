def suman(i,n):
    j = 0
    for k in range(0,i+1):
        j = j+k**n
    return j

i = int(input('Por favor seleccione los primeros n números que desea sumar a un exponente n: '))
if i<0:
    while i<0:
        print('Es imposible sumar los primeros números negativos empezando desde cero \n')
        i = int(input('Por favor seleccione los primeros n números que desea sumar a un exponente n: '))
    n = int(input(f'Por favor seleccione el exponente que desea sumar los {i} números naturales: '))
else:
    n = int(input(f'Por favor seleccione el exponente que desea sumar los {i} números naturales: '))
l = suman(i,n)
print(f'La suma de los primeros {i} números naturales elevados a {n} es: {l}')
