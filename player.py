from time import sleep

input = open("output.txt").read()

blocks = input.split("\n\n")

for block in blocks:
    print("\n" * 20)
    print(block)
    sleep(1)
