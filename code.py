import random
import sys

boxes = random.choice(["box1","box2","box3","box4","box5","box6","box7","box8","box9"])
treasure = boxes

choose =input("enter 1st choice:")
if choose == treasure:
    print("you won")
    sys.exit()
    

guess =input("enter 2nd choice:")
if guess == "boxes":
    print("you won")
    sys.exit()
    
choose =input("enter 3rd choice:")
if (choose == treasure):
    print("you won")
    sys.exit()

print("treasure is in:" , treasure)


