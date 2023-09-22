from time import time, sleep
from random import choice
from colorama import  Fore

#-----------------------------------------------------------

class TimerProgram:
   def __enter__(self):
      global start_t 
      start_t = time()
   def __exit__(self, exc_type, exc_value, exc_traceback):
      time_All = time() - start_t
      
def Speed_function(time):
   global Type_Speed
   Type_Speed = 100*60 // time
   return Type_Speed
      


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
with TimerProgram:
   Tests.choice()
