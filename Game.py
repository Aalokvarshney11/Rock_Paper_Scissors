import random
from colorama import Fore, Style , init

print(" ")
game = input ( f" {Fore.RED} choose one of them  :  stone👊🏻, paper🖐🏻, scissor✌🏻:  { Style.RESET_ALL}")
print(" ")

computer = random.choice([0 ,1 ,-1])
convert = {
    "paper": 0 ,
    "stone":-1 ,
    "scissor":1
    }
reversed = {
   1 : "✌🏻",
   0 : "🖐🏻",
   -1 : "👊🏻"
}
player = {
    "paper": "🖐🏻",
    "stone": "👊🏻" ,
    "scissor":"✌🏻"
   
}


n = convert[game]

print(f"{Fore.LIGHTBLUE_EX} {Style.NORMAL} computer choose the {reversed[computer]} and  you choose {player[game]} \n {Style.RESET_ALL}") 


if(  computer==n):
    print("OHHH SHITTT! 🥲😅 match draw ")
    print(" ")

else:
    if(computer==-1 and n==1):
     print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} OPPSS! 😭💔computer win the game {Style.RESET_ALL}")
     print(" ")

    elif(computer==-1 and n==0):
        print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} HURRYY! 🥳🥇you win the game {Style.RESET_ALL}")
        print(" ")

    elif(computer==0 and n==-1):
        print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} OPPSS! 😭💔computer win the game {Style.RESET_ALL}")
        print(" ")

    elif(computer==0 and n == 1):
        print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} HURRYY! 🥳🥇you win the game {Style.RESET_ALL}")
        print(" ")

    elif(computer == 1 and n==0):
     print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} OPPSS! 😭💔computer win the game {Style.RESET_ALL}")
     print(" ")

    elif(computer == 1 and n == -1):
        print(f"{Fore.LIGHTMAGENTA_EX} {Style.NORMAL} HURRYY! 🥳🥇you win the game {Style.RESET_ALL}")
        print(" ")

    else:
     print("OHHH SHITTT! 🥲😅 match draw ")
     print(" ")