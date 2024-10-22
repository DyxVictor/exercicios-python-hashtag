import time

def cronometro():
    try:
        input('Pressione Enter para iniciar o cronometro')
        inicio = time.time()
        
        input('Pressione Enter para parar o cronometro')
        fim = time.time()
        tempo_decorrido = fim - inicio
        print(f'tempo decorrido: {tempo_decorrido:.2f} segundos')
    except KeyboardInterrupt:
        print('\nCronômetro interrompido')
        
# cronometro()

def cronometros():
    print(f'Cronômetro iniciado!')
    tempo_inicial = time.time()
    try:
        while True:
            tempo_decorrido = time.time() - tempo_inicial
            minutos, segundos = divmod(tempo_decorrido, 60)
            print(f'{int(minutos):02d}:{int(segundos):02d}',end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nCronômetro parado!')
        
cronometros()