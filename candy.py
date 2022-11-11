import random

candy=[0,0,0,0,0,0]

def CANDY():
    c = random.randrange(100)
    a = random.randrange(1,5)
    if c <= 15:
        print("You got ",a," amount of butterfingers")
        candy[0] += a
    elif c <= 35:
        print("You got ",a," amount of Hershey's")
        candy[1] += a
    elif c <= 70:
        print("You got ",a," amount of Peanutbutter cups")
        candy[2] += a
    elif c <= 80:
        print("You got ",a," amount of M&Ms")
        candy[3] += a
    elif c <= 98:
        print("You got ",a," amount of Sour Patch Kids")
        candy[4] += a
    else:
        print("You got a Rock")
        candy[5] += 1
        
for i in range(5):
    CANDY()
print("Final count of candy for each kind: ",candy)
