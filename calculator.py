"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


#welcome statement
#while true loop
#enter math function, two numbers
#input statement >>
#tokenize input using split by space
#if statement and quit if input == "q" "BREAK" loop
#else solve the equation
#return answer 

# Replace this with your code

print("Welcome to the Calculator. Please enter your equation and 2 numbers. Enjoy.")
while True: 
    player_input = input("> ")
    tokens = player_input.split(" ")
    if player_input == "q" or player_input == "Q":
        print("BYE")
        break
    else:
        operater = tokens[0]
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        if operater == "+":
            print(add(num1,num2))
        elif