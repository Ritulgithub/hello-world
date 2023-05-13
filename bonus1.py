data=input("Enter today's:")
mood=input("How do you rate your mood today from 1 to 10?")
thoughts=input=("let your thoughts flow:/n")

with open(f"/journal/{data}.txt","w")as file:
    file.write(mood)
    file.write(thoughts)
