import time 

my_time = int (input("ENter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
     
print("TIME IS UP")

#ANother version or reverse counting
import time 

my_time = int (input("ENter the time in seconds: "))

for x in range(my_time ,0 , -1):
    print(x)
    time.sleep(1)
     
print("TIME IS UP")

#with hours now 
import time 

my_time = int (input("ENter the time in seconds: "))

for x in range(my_time ,0 , -1):
    seconds = x  % 60    
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
     
print("TIME IS UP")


#NUMPAD PROGRAM 
num_pad = ((1, 2, 3),
           (4, 5, 6,),
           (7, 8, 9,),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()


#PYTHON QUIZ GAME

questions = ("How many elements are in the periodic table ?: ",
             "Which animal lays the largest eggs? : ",
             "What is the most abundant gas in the Earths  atmosphere",
             "How many bones are in the human body? : ",
             "Which planet in the solar system is the hottest? : ")

options = (("A. 115", "B. 117", "C. 118", "D. 119"),
           ("A.Whale", "B. Crocodile", "C.  Elephant", "D. Ostrich"),
           ("A.Nitrogen ","B.Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A, 206", "B. 207", "C. 208 ", "D. 209"),
           ("A. Mercury", "B. Venus ","C. Earth" , "D. Mars"),)
           
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D):" ). upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")    
    else :
        print("INCORRECT")
        print(f"{answers[question_num]} is correct answer ")
        
    question_num += 1
