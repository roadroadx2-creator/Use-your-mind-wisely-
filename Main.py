correct_answers = 0
print("use brain")

print("Welcome to the smart puzzle game! Use your intelligence wisely.")
print("Note: The game has three levels: easy, medium, hard.")

goi = input("If you want to start, type Start: ")

if goi.lower() == "start":
    print("Easy level")

    question = "What has teeth but doesn't bite? "
    user_answer = input(question)

    correct_answers = 0

    if user_answer.lower() == "comb":
        correct_answers += 1
        print("Correct!")
    else:
        print("Wrong!")

    print("Number of correct answers:", correct_answers)
question2=input("What is it that walks without feet, flies without wings, and cries without eyes?")
if question2.lower() == "cloud":
    correct_answers += 1
    print("Correct!")
else:
    print("Wrong!")

print("Number of correct answers:", correct_answers)
question3=input("What is something that increases if you take from it, and decreases if you give to it?")
if question3.lower().strip() == "the pit":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question4=input("What is something that breaks as soon as it is spoken?")
if question4.lower().strip() == "silence":
        correct_answers +=1
        print("correct!")
else:
        print("Wrong!")
print("Number of correct answers:", correct_answers)
question5=input("Something we bring to eat, but we never actually eat it (we mean its shell or container)." )
if question5.lower().strip() == "the egg":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question6=input ("What is the thing found in the middle of “Paris”?")
if question6.lower().strip() == "the letter r " :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question7=input("Something that is black when you buy it, turns red when you use it, and becomes gray when it is finished.")
if question7.lower().strip() =="Coal" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)

question8=input("Something that keeps eating constantly and never gets full; if it drinks water, it dies. What is it?")

if question8.lower().strip() == "fire" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:",
correct_answers)

question9 = input("What is it that passes through cities and fields but does not move?...")
if question9.lower().strip() == "roed" :
      correct_answers += 1
      print("Correct!")
else:
      print("Wrong!")
print("Number of correct answers:", correct_answers)
question10=input("What is the “hand” that does not sting and no one is afraid of?")
if question10.lower().strip() =="clock hand" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question11 = input("Something we bring to eat (to prepare) but never eat? ")

if question11.lower().strip() in ["iron", "dishes"]:
    correct_answers += 1
    print("Correct!")
else:
    print("Wrong!")

print("Number of correct answers:", correct_answers)
question12=input("What is it that passes through cities and fields but does not move?")
if question12.lower().strip() =="breakfast":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question13=input("What is it that has a hand but cannot clap?")
if question13.lower().strip() == ["The door" , "the bell"] :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question14=input(" It has a river but no water, and it has cities but no people in them. What is it?")
if question14.lower().strip() =="a mab" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question15=input("It speaks without a mouth and hears without ears. What is it?")
if question15.lower().strip() =="Echo":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question16=input("What is the thing that cannot enter a room unless it is hit on the head?")
if question16.lower().strip() =="Nail":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question17=input("What is something that must be broken before you can use it?")
if question17.lower().strip() =="egg" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question18=input("Something belongs only to you, but other people use it more than you do. What is it?")
if question18.lower().strip() =="name" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question19=input("I have keys but no locks, I have space but no room. You can enter, but you can’t go outside. What am I?")
if question19.lower().strip() =="a keyboard" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question20=input("The more you take, the more you leave behind. What am I?")
if question20.lower().strip() =="footsteps" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question21=input("I’m tall when I’m young, and short when I’m old. What am I?")
if question21.lower().strip() =="candle" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question22=input("What has hands but cannot clap")
if question22.lower().strip() =="a clock" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
question23=input("What gets wetter the more it dries?")
if question23.lower().strip() =="a towel" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
text =" Intermediate level"


centered_text = text.center(50)


print("\033[94m" + centered_text + "\033[0m")

questionx1=input("EN: A man lives on the 10th floor. He takes the elevator down to the ground floor every day. When he comes back, he takes the elevator to the 7th floor and walks the rest of the way. Why?")
if questionx1.lower().strip() == "Because he is a short man and cannot reach the button for the 10th floor.":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)  
questionx2=input("What is the question that you can never answer Yes to? ")
if questionx2.lower().strip() == "are you asleep?" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx3=input("What becomes lighter the more you add to it?")
if questionx3.lower().strip() == "A hole" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx4=input("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
if questionx4.lower().strip() == "A map" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx5=input("What is always in front of you but can’t be seen?")
if questionx5.lower().strip() == "The future" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx6=input("Some months have 31 days, others have 30 days. How many months have 28 days")  
if questionx6.lower().strip() =="All of them (Every month has at least 28 days)." :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx7=input("What can fill a room but takes up no space?")
if questionx7.lower().strip() ==["light" ,"air"] :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx8=input("I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")
if questionx8.lower().strip() == "Fire" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx9=input("What has to be broken before you can use it?")
if questionx9.lower().strip() == "an egg" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questionx10=input("What invention lets you look right through a wall?")    
if questionx10.lower().strip() == "a window" :
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
# -*- coding: utf-8 -*-

import time
import sys


RED = "\033[38;2;255;0;0m"
DARK_RED = "\033[38;2;180;0;0m"
RESET = "\033[0m"
BOLD = "\033[1m"

text = ">> Difficult level <<"


def type_writer(message, color):
    for char in message:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)

border = DARK_RED + "=" * 40 + RESET

print(border)
print()
type_writer(text, RED + BOLD)
print("\n")
print(border)
print("Note: You have reached the difficult level, the level of geniuses.")
questiony1=input ("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
if questiony1.lower().strip =="a mab":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony2=input("A man shaves several times a day, yet he still has a beard. Who is this man?")
if questiony2.lower().strip == "a Barber":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony3=input("What's always coming but never arrives?")
if questiony3.lower().strip =="Tomorrow":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony4=input("You stand before two doors. One leads to freedom, the other to death.There are two guards: one always tells the truth, the other always lies.You may ask only one question to one guard.What do you ask to guarantee freedom?")
if questiony4.lower().strip =="You stand before two doors. One leads to freedom, the other to death.There are two guards: one always tells the truth, the other always lies.You may ask only one question to one guard.What do you ask to guarantee freedom?":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony5=input("Three friends pay $30 for a room ($10 each).Later, the hotel realizes the room costs only $25 and gives $5 back.Each friend gets $1, and $2 is kept as a tip.Now each friend paid $9 → total $27 Plus $2 tip = $29Where is the missing dollar?")
if questiony5.lower().strip =="There is no missing dollar.The $27 already includes the $2 tip.(25 hotel + 2 tip = 27)":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony6=input("A farmer must cross a river with a wolf, a goat, and a cabbage.He can carry only one at a time.Wolf eats goat Goat eats cabbage How does he cross safely?")
if questiony6.lower().strip ==["Take goat", "Return alone" ,"Take wolf", "Take goat" , "Bring goat back", "Take cabbage", "Return alone" ]:
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony7=input("I am not alive, but I grow.I don’t have lungs, but I need air.I don’t have a mouth, but water kills me.What am I? ")
if questiony7.lower().strip =="🔥 Fire":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)
questiony8=input("The more you take, the more you leave behind. What am I?")
if questiony8.lower().strip =="Footsteps":
       correct_answers +=1
       print("correct!")
else:
       print("Wrong!")
print("Number of correct answers:", correct_answers)

if correct_answers <= 8 :
    print (f"Your total points = your level in the game , {correct_answers}/41 (Level beginner)")
elif correct_answers <= 18:
     print (f"Your total points = your level in the game , {correct_answers}/41(Level  middle)")
elif correct_answers <=25:
     print (f"Your total points = your level in the game , {correct_answers}/41(The professional)")
elif correct_answers <=28:
       print (f"Your total points = your level in the game , {correct_answers}/41 (Level legendary)")
elif correct_answers <=35:
       print (f"Your total points = your level in the game , {correct_answers}/41(Genius level)")
elif correct_answers <=40:
      print (f"Your total points = your level in the game , {correct_answers}/41(Genius level very)")
else :
       print (f"Your total points = your level in the game , {correct_answers}/41(Level The master )")                            
                  
