'''

random module ---> Help to generate random values
OTP generation,Story Generation,Game (Rock Papper Scissiors), Number Guessing Game


import random,time
#random number generation --> OTP(time module helps to use time functions)
a = random.randint(1000,9999)
print(a)
for i in range(5):
    time.sleep(2) #sleep(seconds) ---> Helps for waiting period
    print(random.randint(1000,9999))
    #time.sleep(2)


#Playing a Game (Rock Paper Scissiors)
#Two Players --> Game -->

player1 = input("Enter one of these ---> Rock,Paper,Scissors:").lower().strip()
player2 = random.choice(["Rock","Paper","Scissors"]).lower()
#print(player1)
#print(player2)
if player1 == "rock" and player2 == "paper":
    print(f"{player1} vs {player2}")
    print("Player2 Won")
elif player1 == "paper" and player2 == "scissors":
    print(f"{player1} vs {player2}")
    print("Player2 Won")
elif player1 == "scissors" and player2 == "rock":
    print(f"{player1} vs {player2}")
    print("Player2 Won")
elif player1 == player2:
    print(f"{player1} vs {player2}")
    print("Tie")
else:
    print(f"{player1} vs {player2}")
    print("Player1 Won")

when = ['A long back','Once upon a time','Few Years ago']
who = ['Devara','King in the France','Barbie Queen']
what = ['A magical ','PowerFul Hammer','Unlimitied Arrows']
where = ["Far in the Galaxy", "End of Ocean", "In India"]
how = ["War started", "Both fought for 15 days", "Sad Ending"]
print(random.choice(when)+ " " + random.choice(who))
'''

#Business card Generator-->name,email,mobilenumber,websitelink,
#segno-->pip install segno

import segno
print(dir(segno))
from segno import helpers
qr=helpers.make_mecard(name='Kakumanu Lokeshwar',
                       email='lokeshwar5221@gmail.com',
                       phone='+91 7386621771',
                       url="https://www.linkedin.com/in/kakumanu-lokeshwar-32a55a417")
print(qr)
qr.save("Mycard.png",scale=10)













