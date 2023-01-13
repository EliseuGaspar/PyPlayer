from PyPlayer import PlayerMixer as p
from os import system

p.load(dir='D:\Downloads\Musicas')
p.play()

while True:
    #system('cls')
    print("Bem-Vindo ao VínilPlayer Console.")
    print(p.setvolume(0.3))
    decision = input(
        'Use as seguntes teclas para controlar o Player\
        \np) --> para pausar\
        \nup) --> para despausar\
        \nt) --> para tocar\
        \ns) --> para parar\
        \nn) --> para trocar_para_seguinte\
        \nb) --> para trocar_para_anterior\
        \nr) --> para repetir\
        \nqualquer outra) --> para sair do player\
        \n: ')
    
    print(p.duration())
    
    if decision == 'p':
        p.pause()
    elif decision == 'up':
        p.unpause()
    elif decision == 't':
        p.play()
    elif decision == 's':
        p.stop()
    elif decision == 'n':
        p.next_()
    elif decision == 'b':
        p.back()
    elif decision == 'r':
        print(p.tags.full())
    else:
        p.stop()
        break