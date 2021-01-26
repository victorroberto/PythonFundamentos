# Calculadora em Python

print("\n******************* Python Calculator *******************")

print('Selecione o número da operação desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão')

operacao = input('Digite a sua opção (1/2/3/4):')
primeiroNum = float(input('Digite o primeiro número:'))
segundoNum = float(input('Digite o segundo número:'))

def imprime(primeiroNum, segundoNum, operador, resultado):
    print(str(primeiroNum) + operador + str(segundoNum) + ' = ' + str(resultado))
    
if operacao == '1':
    resultado = lambda x, y: x + y
    imprime(primeiroNum, segundoNum, ' + ' , resultado(primeiroNum, segundoNum))
elif operacao == '2':
    resultado = lambda x, y: x - y
    imprime(primeiroNum, segundoNum, ' - ' , resultado(primeiroNum, segundoNum))
elif operacao == '3':
    resultado = lambda x, y: x * y
    imprime(primeiroNum, segundoNum, ' * ' , resultado(primeiroNum, segundoNum))
elif operacao == '4':
    resultado = lambda x, y: x / y
    imprime(primeiroNum, segundoNum, ' / ' , resultado(primeiroNum, segundoNum))
else:
    print('Opção Invalida') 

	
	