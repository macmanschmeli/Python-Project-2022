import sys

argument = sys.argv

print(argument)


if not len(argument) == 3:
    print("Prorgram terminated with error.")
    print("Two arguments must be provided.")
    exit()

print(f"Number of arguments is {len(argument)}")

first_argument = argument[1]
second_argument = argument[2]

try:
    float(first_argument)
    float(second_argument)
except:
    print("Program terminated with errors.\nInput is not in range or a number")