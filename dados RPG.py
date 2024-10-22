import random

dados = {}
valor = []
aceitar = ['sim', 'quero', 'aceito', 'pode ser', 's', 'yes']
replay = 'sim'
melhor = 0

def inserir_dados():
    dados['d2'] = []
    dados['d4'] = []
    dados['d6'] = []
    dados['d8'] = []
    dados['d10'] = []
    dados['d12'] = []
    dados['d20'] = []
    dados['d100'] = []
    for i in range(2):
        dados['d2'].append(i+1)
    for i in range(4):
        dados['d4'].append(i+1)
    for i in range(6):
        dados['d6'].append(i+1)
    for i in range(8):
        dados['d8'].append(i+1)
    for i in range(10):
        dados['d10'].append(i+1)
    for i in range(12):
        dados['d12'].append(i+1)
    for i in range(20):
        dados['d20'].append(i+1)
    for i in range(100):
        dados['d100'].append(i+1)


def roll_dice():
    for j in range(qtde):
        valor.append(random.choice(dados[str(escolha_dado).lower()]))
    return valor 


def show_dice():
    for i in range(qtde):
        print('{}º {} deu: {}'.format(i+1, escolha_dado, valor[i]))

def melhor_resultado(melhor):
    for i in range(qtde):
        if valor[i] > melhor:
            melhor = valor[i]
    print('O melhor resultado foi: {}'.format(melhor))

while replay in aceitar:
    inserir_dados()
    escolha_dado = input('Escolha qual dado voce quer rolar(d2, d4, d6, d8, d10, d12 e d20): ')
    if escolha_dado.lower() in dados:
        qtde = int(input('Quantos dados você quer rodar: '))
        value = roll_dice()
        show_dice()
        melhor_resultado(melhor)
        replay = input('Tentar novamente? ')
    else:
        print('Escolha um dado corretamente')
        replay = input('Tentar novamente? ')

nome = 'Jim Reese'