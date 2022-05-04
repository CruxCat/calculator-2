"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod,)


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
        if tokens[0] == "+":
            print(add(float(tokens[1]),float(tokens[2])))
        elif tokens[0] == "-":
            print(subtract(float(tokens[1]),float(tokens[2])))
        elif tokens[0] == "*":
            print(multiply(float(tokens[1]),float(tokens[2])))
        elif tokens[0] == "/":
            print(divide(float(tokens[1]),float(tokens[2])))
        elif tokens[0] == "square":
            print(square(float(tokens[1])))
        elif tokens[0] == "cube":
            print(cube((float(tokens[1]))))
        elif tokens[0] == "pow":
            print(power(float(tokens[1]),float(tokens[2])))
        elif tokens[0] == "%":
            print(mod(float(tokens[1]),float(tokens[2])))
        else:
            print("Invalid entry. Try again.")