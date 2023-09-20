from time import time, sleep
from random import choice
from colorama import  Fore

#-----------------------------------------------------------

class TimerProgram:
   def __enter__(self):
      global start_t 
      start_t = time()


   

   if len(y) == 100:
      print("calculating speed and accuracy...")
      for i in range(100):
         if x[i] == input_text[i]:
            accuracy += 1
   else: 
      print(Fore.LIGHTRED_EX + "You did not reach 100 Characters.")
      exit()
   return accuracy
         



print(Fore.RED + 'Typing Speedometer')
print(Fore.WHITE)
Tests = ["Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live.",
"A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring whi",
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was bo"]

x = choice(Tests) 
print("Your test case is: ", x)

if 's' in (answer:=input("Press On 's' to Start Typing... and 'e' to exit. . .  ")):
   print("Startng in...")
   for i in range(3,0,-1):
      print(i)
      sleep(1)
