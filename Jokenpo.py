from random import choice
from time import sleep
wins = draws = defeats = 0
while True:
    options= 'pedra', 'papel', 'tesoura'
    pc= choice(options)
    user= int(input('Pedra, Papel ou Tesoura?\n[1] = Pedra\n[2] = Papel\n[3] = Tesoura\n[4] = Sair\nSua opção: '))
    if user==4:
        print('\033[04;31mEncerrando programa...\033[m')
        sleep(2)
        print('=-='*15)
        break
    elif user not in range(1,5):
        print('\33[31;mAssim não vale, escolha apenas entre pedra, papel ou tesoura\33[m.')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        if user==1 and pc=='pedra':
            print('\33[33mEu também escolhi pedra, DEU EMPATE! Teve sorte dessa vez\33[m.')
            draws+=1
        elif user==1 and pc== 'papel':
            print('\33[31mEu escolhi papel. VOCÊ PERDEU!!! era óbvio\33[m.')
            defeats+=1
        elif user==1 and pc=='tesoura':
            print('\33[32mEu escolhi tesoura. NÃÃÃÃÃÃÃÃOOOOO. COMO ASSIM? VOCÊ ME DERROTOU, MEUS PARABÉNS\33[m.')
            wins=+1
        elif user==2 and pc=='pedra':
            print('\33[32meu escolhi pedra. NÃÃÃÃÃÃÃÃOOOOO. COMO ASSIM? VOCÊ ME DERROTOU, MEUS PARABÉNS\33[m.')
            wins+=1
        elif user==2 and pc== 'papel':
            print('\33[33mEu também escolhi papel, DEU EMPATE! Teve sorte dessa vez\33[m.')
            draws+=1
        elif user==2 and pc=='tesoura':
            print('\33[31mEu escolhi tesoura. VOCÊ PERDEU!!! era óbvio\33[m.')
            defeats+=1
        elif user==3 and pc=='pedra':
            print('\33[31mEu escolhi pedra. VOCÊ PERDEU!!! era óbvio\33[m.')
            defeats+=1
        elif user==3 and pc=='papel':
            print('\33[32mEu escolhi papel. NÃÃÃÃÃÃÃÃOOOOO. COMO ASSIM? VOCÊ ME DERROTOU, MEUS PARABÉNS\33[m.')
            wins+=1
        elif user==3 and pc=='tesoura':
            print('\33[33mEu também escolhi tesoura, DEU EMPATE! Teve sorte dessa vez\33[m.')
            draws+=1
    print('=-='*15)
print('\033[04;34mPrograma encerrado com sucesso.\033[m')
print('Seu recorde foi de: ')
print(f'\033[04;32m{wins} Vitórias\33[m', end= ' - ')
print(f'\033[04;33m{draws} Empates\033[m', end=' - ')
print(f'\033[04;31m{defeats} Derrotas\33[m')