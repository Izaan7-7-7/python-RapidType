import pyautogui as pag
from time import sleep

print("-"* 80)
print("                       WELCOME TO MESSAGE SPAMMER         ")
print("-"*80)

print("OPEN ANY MESSAGING APP AND OPEN THE CONTACT YOU WANT TO SEND THE MESSAGE")
msg = input("ENTER THE MESSAGE YOU WANT TO SEND:")
count = int(input("HOW MANY TIMES YOU WANT THE MESSAE TO BE SENT:"))

print("INITIATING ATTACK IN 5 SECONDS!")
sleep(5)
try:
 for i in range(count):
     pag.write(msg)
     pag.press("enter")

except ValueError:
    count = int(input("HOW MANY TIMES YOU WANT THE MESSAGE TO BE SENT:"))

print("DONE")    