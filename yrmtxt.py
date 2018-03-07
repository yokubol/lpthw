from sys import argv
import time
import random

script, filename = argv

print("Opening the file...")
time.sleep(2)
target = open(filename, 'w')
print("Success.")
time.sleep(1)

random_number = random.randint(1, 324)
print(f"Connecting to NASA supercomputer RX{random_number}...")
time.sleep(2)

print("Initiate HyperDeletion software. Use under NASA supervision!!!.")
time.sleep(1)

print("Deleting all texts in the file...")
time.sleep(1)

target.truncate()
print("Done.")
time.sleep(1)
