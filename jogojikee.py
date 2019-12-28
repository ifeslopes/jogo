import time
import os
import random
from  random import randint
from  time import sleep
n=0
b=0 #11
dano=""
play1=10
play2=10
t=15
r=0
g=0.01
round_play1 = 0
round_play2 = 0
v1=""
v2=""
lista = ["PEDRA","PAPEL","TESOLRA"]


c=True
while c:
    p1=0
    p2=0
    os.system("clear") or None
    print("",end="\r")
    print("\033[42m \033[m"*play1+"\033[41m \033[m"*b,end="")
    
    #if dano=="play1":
    
    print(" PLAY1 VS COMP ",end="")
    
    print("\033[42m \033[m" * play2 + "\033[41m \033[m" * n,end=" ")

    
    print()
    print(f"{v1}                           {v2}")
    u=True
    comp = randint(0,2)
    print()
    print(
        '''ESCOLHA UMA DAS OPEÇES
[0] PEDRA
[1] PAPEL
[2] TESOLRA''')
    print()
 
    #jogador= int(input("Escolha...: "))
    jogador=randint(0,2)
    if jogador >2:
        print("valor invalido")
        sleep(1)
        system("clear") or None 
        
    else:
        print("JO")
        sleep(1)
        print("KEEEE...")
        sleep(1)
        print("POOOO!")
        sleep(1)
        
        print(f"jogador escolheu >>> {lista[jogador]}")
        print(f"COMPUTADIR escolheu >>>{lista[comp]}")
        if comp ==0:
            if jogador ==0:
                print("EMPATE")
                
                
                
            elif jogador ==1:
                print("JOGADOR VENCE")
                p1=+1
                
            elif jogador ==2:
                print("COMPUTADOR VENCE")
                p2=+1
                
        
        elif comp == 1:
            if jogador ==0:
                print("COMPUTADOR VENCE")
                p2=+1
                
            elif jogador ==1:
                print("EMPATE")
                
                
                
                
            elif jogador ==2:
                print("JOGADOR VENCE")
                p1=+1
                
        
        elif comp ==2:
            if jogador ==0:
                print("JOGADOR VENCE")
                p1=+1
                
            elif jogador ==1:
                print("COMPUTADOR VENCE")
                p2=+1
                
                
            elif jogador ==2:
                print("EMPATE")
        sleep(1.3)
                
        
    if round_play1==2:
        print("******PLAY1 GANHOU!******")
        break
    if round_play2==2:
        print("******COMPUTADOR GANHOU!*****")
        break
            
            

    while u:
    
        s=(" "*t)
        d=(" "*r)

        
        if r==5:
            #print(f"{p1} {p2}")
            print()
            if p1>p2:
                
                print("\033[43m")
                time.sleep(0.01)
            
                os.system("clear") or None
                
                print("\033[40m")
                
                os.system("clear") or None
                
                print(f"\n \n        PLAY1: {lista[jogador]} VENCE {lista[comp]}!")
                play2-=2
                n+=2
                u=False
                
                time.sleep(2)
                r=0
                t=15
                g=0.15
            
                
                
            elif p2>p1:
                
                print("\033[43m ")
                #time.sleep(1)
                
                
                
                os.system("clear") or None
                
                print("\033[40m")
                
                os.system("clear") or None
                
                print(f"\n\n       \n \n        COMP: {lista[comp]} VENCE {lista[jogador]}!")
                play1-=2
                b+=2
                u=False
                #input()
                time.sleep(3)
                r=0
                t=15
                g=0.01
            
                
            else:
                print("\033[43m ")
                #sleep(1)
                print("Deu empate!")
                r=0
                t=15
                g=0.01
                u=False
                os.system("clear")
                print("\033[40m")
                os.system("clear")
                print(f"\n \n         EMPATE!")
                
                
        t-=2
        r+=1
        g+=0.15
    
        time.sleep(g)
        #os.system("clear") or None
    
    