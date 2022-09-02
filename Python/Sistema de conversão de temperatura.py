nova_conversão = 'S'
while nova_conversão == 'S':
    print('''
    Menu Principal

    [ 1 ] Celsius para Kelvin
    [ 2 ] Celsius para Fahrenheit
    [ 3 ] Kelvin para Celsius
    [ 4 ] Kelvin para Fehrenheit
    [ 5 ] Fahrenheit para Celsius
    [ 6 ] Fahrenheit para Kelvin
    [ 0 ] SAIR
    ''')
    opcao = int(input('Escolha uma das opçẽos acima: '))

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6:
        valor = float(input('Digite o valor da tempratura em graus [Celsius | Kelvin | Fahrenheit]: '))
        if opcao == 1:
            if valor > -273.15:
                transfromacao = valor + 273.15
                print(f'Os {valor}° Celsius para Kelvin fica {transfromacao :.2f}°K')
            else:
                print('A menor temperatura em Celsius é o -273,15°C absoluto. \nVocê colocou uma temperatura menor que -273,15°C')
    
        elif opcao == 2:
            if valor > -273.15:
                transfromacao = (valor * 9/5) + 32
                print(f'Os {valor}° Celsius para Fehrenheit fica {transfromacao :.2f}°F')
            else:
                print('A menor temperatura em Celsius é o -273,15°C absoluto. \nVocê colocou uma temperatura menor que -273,15°C')
        
        elif opcao == 3:
            if valor > 0:
                transfromacao = valor - 273.15
                print(f'Os {valor}° Kelvin para Celsius fica {transfromacao :.2f}°C')
            else:
                print('A menor temperatura em Kelvin é o 0 absoluto. \nVocê colocou uma temperatura menor que zero.')
        
        elif opcao == 4:
            if valor > 0:
                transfromacao = (valor - 273.15) * 9/5 + 32
                print(f'Os {valor}° Kelvin para Fehrenheit fica {transfromacao :.2f}°F')
            else:
                print('A menor temperatura em Kelvin é o 0 absoluto. \nVocê colocou uma temperatura menor que zero.')
        
        elif opcao == 5:
            if valor > -459.67:
                transfromacao = (valor - 32) * 5/9
                print(f'Os {valor}° Fehrenheit para Celsius fica {transfromacao :.2f}°C')
            else:
                print('A menor temperatura em Fehrenheit é o -459,67°F absoluto. \nVocê colocou uma temperatura menor que -459,67°F')
        elif opcao == 6:
            if valor > -459.67:
                transfromacao = (valor - 32) * 5/9 + 273.15
                print(f'Os {valor}° Fehrenheit para Kelvin fica {transfromacao :.2f}°K')
            else: 
                print('A menor temperatura em Fehrenheit é o -459,67°F absoluto. \nVocê colocou uma temperatura menor que -459,67°F')
    elif opcao == 0:
        exit()
    else:
        print('OPÇÃO INVALIDA!')
        
    
    nova_conversão = input('\nDeseja fazer outra conversão (S/N)? ').strip().upper()
    while nova_conversão not in 'SN':
        nova_conversão = input(
        '''
                TENTE NOVAMENTE
        Deseja fazer outra conversão (S/N) ? 
        ''').strip().upper()
