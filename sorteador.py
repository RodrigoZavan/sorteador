import PySimpleGUI as sg
import random

sg.theme('DarkAmber')   # Cor da janela
# Layout da janela
layout = [  [sg.Text('Preencha com os com a quantidade de números a serem sorteados!')],
            [sg.Text('Total de números a serem sorteados'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Criando a janela
window = sg.Window('Sorteador', layout)
# Fica em loop enquando o usuário não clicar em cancelar
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # Verifica se o usuario clicou em cancelar para sair do loop
        break
    num = int(values[0])
    sg.popup('Número sorteado', random.randrange(1,num+1))
    num = 0

window.close()