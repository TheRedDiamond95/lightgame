import random
import time

print("funny game")
print("turn the light on")
while True:
  switchAction=int(input("type '1' to turn on the switch"))
  if switchAction==1:
    switchState=1
  else:
    switchState=0
  
  randomchance1=random.randint(0,100)
  if randomchance1==69:
    print("the light is somehow liked. you win")
    round1=1
    break
  else:
    (switchState)==0 
    time.sleep(random.randint(0,5))
    print("the light is not liked. it is now off") 
    (switchAction)==0
    print("turn on the light again")

