print("Welcome to my quiz game!...")
quiz=input("Do you play quiz game?").lower()
    
    
if quiz != "yes" :
     quit()
print("ok, Let's play")
score=0
answer=input("What is the capital of Japan?:").lower()
if answer == "tokyo" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("Which is the longest river in the world?:").lower()
if answer == "the nile" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")

answer=input("Which planet is known as the Red Planet?: ").lower()
if answer == "mars " :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What is the largest ocean on Earth?:").lower()
if answer == "the pacific ocean " :
    print("Correct!")
    score += 1
else :
    print("Incorrect")

    
answer=input("Which continent is the Sahara Desert located on? :").lower()
if answer == "africa " :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("How many players are there in a cricket team?:")
if answer == "11" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What is the national flower of India?:").lower()
if answer == "lotus" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What is the smallest state in India by area?: ").lower()
if answer == "goa" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("Who is the Missile Man of India?: ").lower()
if answer == "dr. a.p.j. abdul kalam" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What gas do living creatures need to breathe? :").lower()
if answer == "oxygen" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What is the process by which plants make their food? :").lower()
if answer == "photosynthesis" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("What is the largest organ in the human body? : ").lower()
if answer == "skin" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input(" What is the force that pulls objects towards the Earth? :").lower()
if answer == "gravity" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("Which part of a plant absorbs water and nutrients from the soil? :").lower()
if answer == "roots" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")
    
answer=input("When did India get independence? :")
if answer == 1947 :
    print("Correct!")
    score += 1
else :
    print("Incorrect")

print(f"You Got {score} questions correct")