"""This application-as-a-service script performs following operations with zero:
- adding to another number
- subtracting from another number
- muptiplying by another number
- dividing by another number

Created on 9 April 2024 by Dmitrii Kosintsev as a part of MLH GHW
Challenge: Useless application with API"""

import requests
import json
import time

def calculate():
    # Ask the user for the number to evaluate
    number = input("Enter your number: ")
    exit = False

    # Use a loop to prevent the user from entering invalid operations
    while exit == False:
        op = input("Enter the operation (+, -, *, /): ")

        # Use time.sleep() to prevent the user from sending requests too often
        # The service provides evaluations every 10 seconds
        print("Establishing connection...")
        time.sleep(3)
        print("Connected!")
        time.sleep(2)
        print("Calculating...")
        time.sleep(3)

        # Check whether the entered operation was correct
        match op:
            
            # Do division or multiplication
            case "/" | "*":
                exit = True
                url = f"http://api.mathjs.org/v4/?expr=0{op}{number}"
                break
            
            # Do addition
            case "+":
                exit = True
                url = f"http://api.mathjs.org/v4/?expr=0%2B{number}"
                break
            
            # Do subtraction
            case "-":
                exit = True
                url = f"http://api.mathjs.org/v4/?expr={number}{op}0"
                break

            # Handle invalid operations
            case _:
                print("Invalid operation. Please try again.")
    
    # Parse the request and recieved JSON file
    response = requests.get(url)
    result = json.loads(response.text)
    return result # Return the result

print("The answer is:", calculate())