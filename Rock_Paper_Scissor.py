x = input("Rock, Paper or Scissor ? ").lower()
print(x)

import random
number = random.randint(1,3)
print(number)
ans = ""
if number == 1 :
    ans = "Rock"

elif number == 2 :
    ans="Paper"
else :
    ans="Scissor"

ans = ans.lower()

print("User Selected:", x, "kl")
print("Bot Selected:", ans, "ew")


if (ans == 'rock' and x == 'scissor') or (ans == 'scissor' and x == 'paper') or (ans == 'paper' and x == 'rock'):
    print ("Computer wins")
elif (x == 'rock' and ans == 'scissor') or (x == 'scissor' and ans == 'paper') or (x == 'paper' and ans == 'rock'):
    print ('user wins')
else :
    print("Draw")    

