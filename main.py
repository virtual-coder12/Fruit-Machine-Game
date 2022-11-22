import random
import time

print("Welcome to our Fruit Machine game.\n You begin with 100 credits and each turn costs 20 credits. \n If three of the symbosl are the same, you win 100 credits \n and if you roll 3 Bells, you receive 500 credits.")
print("\n")

credits = 100
#Placing all symbols in group


#Looping to print 3 symbols for the slot machine
Continue = True
while credits >= 20 or Continue:
   
  
  x = input("Do you want to roll? ")
  ss = random.choice(["Cherry", "Bell", "Lemon", "Orange", "Star","Skull"])
  s2 = random.choice(["Cherry", "Bell", "Lemon", "Orange", "Star","Skull"])
  s3 = random.choice(["Cherry", "Bell", "Lemon", "Orange", "Star","Skull"])
  if x == "Yes" or "yes" or "Y" or "y":
    a = print(ss)
    b = print(s2)
    c = print(s3)
    credits -= 20
  
    time.sleep(0.3)


    if ss == s2 or s2 == s3 or (s3 == ss):
     credits += 50
    elif ss == s2 == s3 :
     credits += 100
    elif ss and s2 and s3 == str("Bell"):
      credits += 500
    elif ss and s2 or s2 and s3 or s3 and ss == "Skull":
      credits -= 100

  print("\n")

  print("You have: ")  
  print("£" + str(credits))


if credits == 0:
  print("You have ran out of credits.")
  exit()