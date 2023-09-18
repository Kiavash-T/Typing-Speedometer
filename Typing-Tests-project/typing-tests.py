from time import time, sleep
from random import choice
from colorama import  Fore

# -------------------------------------------------------------------

print(Fore.RED + 'Typing Speedometer')
print(Fore.WHITE)

Tests = ["Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live.",
"A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring whi",
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was bo"]

x = choice(Tests) 
print("Your test case is: ", x)
