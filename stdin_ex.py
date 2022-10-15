import sys

input_data=sys.stdin

for line in input_data:
    if line.strip() == 'exit':
        print("Got to exit. Stopping the program")
        exit(0)
    else:
        print(f"Received : {line}")
#input()