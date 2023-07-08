## This program determines if a number is composite or if it is prime. Also, determine by prime numbers is composed
def primo(num): ## Recursion to know if a number is prime or not
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
        else:
            count=count
    if count==2:
        crit=1
    else:
        crit=0
    return crit
n=0
con=None
while n==0:
    if con==None:
        con=int(input('Por favor digite un número que desee evaluar: '))
    elif con<0:
        print(f'El número seleccionado es negativo, por lo cual no tendría sentido evaluar esta condición')
        con = int(input('Por favor digite un número que desee evaluar: '))
    elif con==0 or con==1:
        print(f'El número {con} no es considerado número primo o compuesto.')
        n+=1
    else:
        if primo(con)==1:
            print(f'El número digitado ({con}) es un número primo.')
            n+=1
        else:
            primos=[]
            for i in range(2,con):
                if con%i==0 and primo(i)==1:
                    primos.append(i)
                else:
                    n+=1
            print(f'El número digitado ({con}) es compuesto por los siguientes números primos: \n {primos}')
            n+=1
