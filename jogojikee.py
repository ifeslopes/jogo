from  random import randint
from  time import sleep
from  os import system
c=0   #contador  do computador
p=0   #contador  do computador
def jokepo(x): #função principal1
    
    lista = ["PEDRA","PAPEL","TESOLRA"] #aquiteste git
    comp = randint(0,2)
 
    jogador= int(x)
    if jogador >2:
        print("valor invalido")
        sleep(1)
        system("clear") or None 
        
    else:
        print("JO")
        sleep(1)
        print("KEEEE...")
        sleep(2)
        print("POOOO!")
        sleep(1)
        
        print(f"jogador escolheu >>> {lista[jogador]}")
        print(f"COMPUTADIR escolheu >>>{lista[comp]}")
        if comp ==0:
            if jogador ==0:
                print("EMPATE")
            elif jogador ==1:
                print("JOGADOR VENCE")
            elif jogador ==2:
                print("COMPUTADOR VENCE")
        
        elif comp == 1:
            if jogador ==0:
                print("COMPUTADOR VENCE")
            elif jogador ==1:
                print("EMPATE")
            elif jogador ==2:
                print("JOGADOR VENCE")
        
        elif comp ==2:
            if jogador ==0:
                print("JOGADOR VENCE")
            elif jogador ==1:
                print("COMPUTADOR VENCE")
            elif jogador ==2:
                print("EMPATE")
    
    
while True:
    print()
    print('''ESCOLHA UMA DAS OPEÇES
    [0] PEDRA
    [1] PAPEL
    [2] TESOLRA''')
    jogador= int(input("Escolha...: "))
    jokepo(jogador)