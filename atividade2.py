while True:
    nome = input('Digite um nome (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break
    print(f'Nome digitado: {nome}')

print('\nNúmeros pares de 1 a 20:')
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

