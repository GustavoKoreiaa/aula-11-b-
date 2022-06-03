qtde = int(input('Informe Quantos Cigarros você foma por dia: '))
anos = int(input('Informe por quantos anos você: '))

soma = qtde*(anos*365)
minutos = soma*10

subtrai = (minutos/60)/24

print('Você tem %.2f dias a menos de vida' %subtrai)
#--------------------segundo codigo-------------------
print('----Calculadora de Dias de Carro Alugado----')

d = int(input('Quantos Dias o Carro Ficou Alugado: '))
k = float(input('Quantos Km foram rodados: ').replace(',','.'))

paga=(d*60)+(k*0.15)

print('O valor a ser pago é R${:.2f} devido a {:.0f} dias de aluguel e {:.0f} Km rodados'.format(paga,d,k))

#-------------------primeiro codigo-----------------------
print('-----Conversor Temperatura Celsius para Fahrenheit-----')

c = float(input('Insira a Temperatura em Celsius: ').replace(',','.'))
f = (9*(c/5)+32)
print('Fahrenheit : {:.2f}'.format(f))

print('\n\n----Conversor Temperatura Fahrenheit para celsius----')

f = float(input('Insira a Temperatura em Fahrenheit: ').replace(',','.'))
c = ((f-32)/1.8)
print('Celsius : {:2f}'.format(c))