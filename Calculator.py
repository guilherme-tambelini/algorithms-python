#Basic calculator program using Python
#Create by Guilherme Sanches Tambelini
#Version 1.0

import datetime

#Funções Não funcionais
def escreveLog(texto):
	log = "C:\\Alpha\\Algoritimos\\Python\\Calculadora\\Log-Calculator.txt"
	try:
	    fp = open(log)
	except IOError:
	    #Se nao existir, criar o arquivo
	    fp = open(log, 'w+')
	log = open(log, "a")
	log.write(str(datetime.datetime.now()) + " - " + texto)
	log.write("\n")
	log.close()

def escreveTextoResultado(texto):
	print("\n")
	print(texto)
	print("\n")
	
escreveLog("Início")
continua = "s"

print("\n******************* Python Calculator *******************")
while (continua == "s"):
	print("\nSelecione o número da operação desejada: \n")
	print("1 - Soma")
	print("2 - Subtração")
	print("3 - Multiplicação")
	print("4 - Divisão")
	print("5 - Potencia")
	
	while True:
		try:
			escolha = int(input("\nDigite sua opção (1/2/3/4/5): "))
			escreveLog(str("opção escolhida: " + str(escolha))) #log
			break
		except ValueError as e1:
			print("\nOpção Inválida!")
			escreveLog("Opção Inválida!")
			escreveLog(str(e1))
		except Exception as e2:
			print("\nOpção Inválida!")
			escreveLog("Opção Inválida!")
			escreveLog(str(e2))

	if (escolha == 1) or (escolha == 2) or (escolha == 3) or (escolha == 4):
		texto = input("\nDigite o primeiro número: ")
		try:
			num1 = int(texto)
		except ValueError:
			print("\nValor Inválido: " + texto)
			continue

		texto = input("\nDigite o segundo número: ")
		try:
			num2 = int(texto)
		except ValueError:
			print("\nValor Inválido: " + texto)
			continue
	
	if (escolha == 5):
		texto = input("\nDigite a base: ")
		try:
			num1 = int(texto)
		except ValueError:
			print("\nValor Inválido: " + texto)
			continue

		texto = input("\nDigite o expoente: ")
		try:
			num2 = int(texto)
		except ValueError:
			print("\nValor Inválido: " + texto)
			continue

	if (escolha == 1):
		resultado = (lambda x,y: x + y) (num1, num2)
		escreveTextoResultado(str(num1) + "+" + str(num2) + "=" + str(resultado))
		escreveLog(str(num1) + "+" + str(num2) + "=" + str(resultado))
	
	elif (escolha == 2):
		resultado = (lambda x,y: x - y) (num1, num2)
		escreveTextoResultado(str(num1) + "-" + str(num2) + "=" + str(resultado))
		escreveLog(str(num1) + "-" + str(num2) + "=" + str(resultado))
	
	elif (escolha == 3):
		resultado = (lambda x,y: x * y) (num1, num2)
		escreveTextoResultado(str(num1) + "*" + str(num2) + "=" + str(resultado))
		escreveLog(str(num1) + "*" + str(num2) + "=" + str(resultado))
	
	elif (escolha == 4):
		try:
			resultado = (lambda x,y: x / y) (num1, num2)
			escreveTextoResultado(str(num1) + "/" + str(num2) + "=" + str(resultado))
			escreveLog(str(num1) + "/" + str(num2) + "=" + str(resultado))
		except ZeroDivisionError as e:
			escreveTextoResultado("Divisao por zero")
			escreveLog("Exception ZeroDivisionError:Divisao por zero - " + str(num1) + "/" + str(num2))
			escreveLog(str(e))
	
	elif (escolha == 5):
		resultado = str(potencia(num1, num2))
		escreveTextoResultado(str(num1) + " elevado a " + str(num2) + " = " + str(resultado))
		escreveLog(str(num1) + " elevado a " + str(num2) + " = " + str(resultado))
	else:
		escreveTextoResultado("Opção Inválida!")
		escreveLog("Opção Inválida: " + str(escolha))
	
	continua = str(input("\nDeseja continuar? Opções [s/n]: "))

else:
	escreveTextoResultado("Fim")
	escreveLog("Fim")