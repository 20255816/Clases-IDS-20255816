"""state = input()
while state == state:
    if state == 'conectado':
        while state == 'conectado':
            print('Ola Ivan')
            state = input()
    elif state == 'desconectado':
        while state == 'desconectado':
            print('Ol...')
            state = input() """
            
state = input()
while state == 'conectado' or state == 'desconectado':
    if state == 'conectado':
        while state == 'conectado':
            print('Ola Ivan')
            state = input()
    elif state == 'desconectado':
        while state == 'desconectado':
            print('Ol...')
            state = input()
            
