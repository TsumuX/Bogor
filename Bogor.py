import time
import random

nama = input("your name=")

print("wait...")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

rand = random.randint(0, 100)

print(nama, "=", rand,"%")

if(rand <=20):
    print("status: normal")
    exit()
 
if(rand <=50):
    print("status: hati hati")
    exit()
    
if(rand >=50):
    print("status: bogor")
    exit()
exit()
clear()
