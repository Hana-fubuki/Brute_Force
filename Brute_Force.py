# imported libraries
import random
import time

# Word or phrase to be brute forced
target = list("String you want to brute force")
# current holding
current = [""] * len(target)
i = 0
while i < len(target):
    #This only supports ascii charters 32 - 126
    #Can be changed by modifying below
    current[i] = chr(random.randint(32, 126))
    if current[i] == target[i]:
        i += 1
    print("".join(current))
    time.sleep(.005)