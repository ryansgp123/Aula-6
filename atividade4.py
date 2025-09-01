tentativas = 0
while True:
    tentativas += 1
    print(f'Tentativa de saque: {tentativas}')
    if tentativas == 3:
        print('Caixa bloqueado. Limite de tentativas atingido.')
        break

