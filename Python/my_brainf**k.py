import os, sys

memory = [21]
i = 0
def print_memory():
    string = ""
    for j in memory:
        string += chr((j-21)%101+22)
    print(string)
file = open(sys.argv[1], "r")


for _inp in file.readlines():
    for inp in _inp:
        if inp == "+":
            memory[i] +=1
        elif inp == "-":
            memory[i] -=1
        elif inp == ">":
            i += 1
            while len(memory) <= i:
                memory.append(21)
        elif inp == "<":
            i -= 1
        elif inp == "$":
            print_memory()
        elif inp == ";":
            memory.clear()
            memory.append(21)
            i = 0
