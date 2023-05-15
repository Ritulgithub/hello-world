data=input("Enter today's:")
mood=input("How do you rate your mood today from 1 to 10?")
thoughts=input=("let your thoughts flow:/n")

with open(f"../journal/{data}.txt","w")as file:
    file.write(mood)
    file.write(thoughts)
while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")

user_prompt="Enter a todo:"
todo1=input(user_prompt)
todo2=input(user_prompt)
todo3=input(user_prompt)
todos= [todo1,todo2,todo3,"hello"]
print (todos)


user_prompt="Enter a todo:"

todos= []
while True:
    todo=input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)

password = input("Enter a new password: ")

result= []

if len(password) > 7:
    result.append("Great password there!")
else:
    result.append("Your password is weak.")

print(result)
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    return maximum
grades= get_max()
print(grades)

def get_average():
    with open ("files/data.txt", 'r') as file:
     data=file.readlines()

values=data[1:]
values=[float(i)for i in values]

average_local=sum(values)/len(values)
return average_local

average = get_average()
print (average)

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

def circle_ara(r):
    pi = 3.14
    area = 2*pi * r**2
    return area


def get_area(x=10):
    return x * 2


area = get_area()
print(area)

def get_area(x=10):
    return x * 2


area = get_area(x=1)
print(area)


def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


birth = int(input("What is your year of birth?"))
age = get_age(birth)
print(age)