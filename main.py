import time
import itertools
import threading
import sys
import urllib.request

done = False

def helloBarista():
  print('Hello there, let us get started.')
  print('To get started, type the function Coffee_AI() in the console.')

def Coffee_AI():
  #Greeting the User!
  print('Hello there human!')

  time.sleep(1)
        
  print('Good day to you -Coffee Barista AI')

  time.sleep(1)
  
  #Asking for the User's name?
  name = input("What is your name?\n")

  time.sleep(1)

  print("Hello " + name + ", thank you so much for coming in today.\n\n")

  menu = "Black Coffee, Espresso, Latte, Cappucino"

  print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

  order = input()

  CoffeePrice = str(3.00)
  EspressoPrice = str(4)
  LattePrice = str(3.75)
  CappucinoPrice = str(4)

  if order == 'Black Coffee':
    print("A " + order + " costs exactly = " + CoffeePrice) 
  elif order == 'Espresso':
    print("A " + order + " costs exactly = " + EspressoPrice)
  elif order == 'Latte':
    print("A " + order + " costs exactly = " + LattePrice)
  elif order == 'Cappucino':
    print("A " + order + " costs exactly = " + CappucinoPrice)
  
  else: print("Sorry about that, we don't serve that " + order)
  
  #print("A " + order + " costs exactly " + )

  #taking 2 seconds to load process to retrieve money from human
  time.sleep(2)

  print("Okay retrieving your money, .....")

  done = False
  #here is the animation
  def animate():
      for c in itertools.cycle(['|', '/', '-', '\\']):
          if done:
              break
          sys.stdout.write('\rloading ' + c)
          sys.stdout.flush()
          time.sleep(0.1)
      sys.stdout.write('\rDone!     ')
  
  t = threading.Thread(target=animate)
  t.start()
  
  #long process here
  time.sleep(10)
  done = True

  time.sleep(1)
  #taking 10 seconds to retrieve money from human
    
  print("Alright, thanks for the money " + name)

  print("""
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
        """)
  print("""
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
        """)
  print("""
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
        """)
  print("""
___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
        """)

  time.sleep(1)

  print("\nSounds good " + name + ", we'll have that " + order + " ready for you in a moment.")

  done = False
  #here is the animation
  def animate():
      for c in itertools.cycle(['|', '/', '-', '\\']):
          if done:
              break
          sys.stdout.write('\rloading ' + c)
          sys.stdout.flush()
          time.sleep(0.1)
      sys.stdout.write('\rDone!     ')
  
  t = threading.Thread(target=animate)
  t.start()
  
  #long process here
  time.sleep(8)
  done = True

  time.sleep(1)

  print("Here is your beverage, Enjoy! :)")

  time.sleep(1)
  
  print("""
            (  ) 
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\___
""")

  print("Thanks for playing the game. The End.")


helloBarista()