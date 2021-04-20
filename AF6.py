'''
1) Criar um Algoritmo que imprima todos os números de 1 até 100, inclusive, e a soma de todos eles. 
2) Criar um Algoritmo que leia um número(NUM), e depois leia NUM números inteiros e imprima o maior deles. Suponha que todos os números lidos serão positivos. 
3) Criar um Algoritmo que leia um número(NUM), e depois leia NUM números inteiros e imprima o menor deles. 
4) Criar um Algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números impares no intervalo aberto e seu somatório. 
Suponha que os dados digitados são para um intervalo decrescente, ou seja, o primeiro valor é maior que o segundo.
5) Escreva um Algoritmo que determine todos os divisores de um dado número N

'''
escolha = int(input("Escolha a atividade (1-5):"))
if(escolha>5 or escolha<1):
    exit("Atividade não existente")
'''
---------------------------------------------ALGORITMO Exercício 1:

#VARIAVEIS
numerosoma = 0
contador = 0

#PROGRAMA
enquanto contador < 100 faça
    contador += 1
    imprima(contador)
    numerosoma += contador
fim enquanto
imprima(numerosoma)
exit()
'''
numerosoma = 0
if(escolha==1):
    contador = 0
    while (contador < 100):
        contador += 1
        print(contador)
        numerosoma += contador
    print("A soma é:",numerosoma)
    exit()
'''
---------------------------------------------ALGORITMO Exercício 2:

#VARIAVEIS
numero = 0
contador = 0
numeromaior = 0
numerolido = 0

#PROGRAMA
numero = leia(numero)
enquanto contador < numero
    contador += 1
    numerolido = leia("numero Digitado")
    se numeromaior < numerolido
        numeromaior = numerolido
    fim se
imprima(numeromaior)
fim enquanto
exit()
'''
contador = 0
numeromaior = 0
if(escolha==2):
    numero = int(input("Digite um Número (pequeno por favor): "))
    while (contador < numero):
        contador += 1
        numerolido = int(input("Digite mais um Número: "))
        if (numeromaior < numerolido):
            numeromaior = numerolido
    print("O maior Número é: ",numeromaior)
    exit()
'''
---------------------------------------------ALGORITMO Exercício 3:
#VARIAVEIS
numero = 0
contador = 0
numeromenor = 0
numerolido = 0

#PROGRAMA
numero = leia(numero)
enquanto contador < numero
    contador += 1
    numerolido = leia("numero Digitado")
    se numeromenor > numerolido
        numeromenor = numerolido
    fim se
imprima(numeromenor)
fim enquanto
exit()
'''
contador = 0
numeromenor = 1000000000000000000000000000000000000000000000000
if(escolha==3):
    numero = int(input("Digite um Número: "))
    while (contador < numero):
        contador += 1
        numerolido = int(input("Digite outro Número: "))
        if(numeromenor > numerolido):
            numeromenor = numerolido
    print("O menor Número é: ",numeromenor)
    exit()
'''
---------------------------------------------ALGORITMO Exercício 4:
#VARIAVEIS
numeromenor = 0
numeromaior = 0
numerosoma = 0

#PROGRAMA
numeromenor = leia("numero menor")
numeromaior = leia("numero maior")
enquanto numeromenor < numeromaior faça
    se numeromenor mod 2 != 0
        imprima(numeromenor)
    fim se
    numerosoma += numeromenor
fim enquanto
imprima(numerosoma)
'''
numerosoma = 0
if(escolha==4):
    numeromenor = int(input("Digite um Número: "))
    numeromaior = int(input("Digite um Número maior que o anterior: "))
    while(numeromenor < numeromaior):
        if ((numeromenor%2) != 0):
            print("Número ímpar! -",numeromenor)
            numerosoma += numeromenor
        numeromenor += 1
    print("A soma de todos os números é:",numerosoma)
'''
---------------------------------------------ALGORITMO Exercício 5:
#VARIAVEIS
numero = 0
contador = 1

#PROGRAMA
numero = leia(numero)
enquanto contador < numero faça
    se numero mod contador == 0
        imprima(contador)
    fim se
    contador += 1
fim enquanto
'''
contador = 1
if(escolha==5):
    numero = int(input("Digite um Número: "))
    while(contador < numero):
        if(numero % contador == 0):
            print(contador)
        contador += 1