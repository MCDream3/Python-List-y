import random, nump
T = []
for i in range(40):
    T.append(random.randint(10, 100))

print(f"{T}")

#Zad1

print(f"{max(T)}")

#Zad2

print(f"{min(T)}")

#Zad3

print(f"{len(T)}")

#Zad4
#Zad5

#Zad6

print(f"{T.count(max(T))}")

#Zad7

print(f"{T.count(min(T))}")

#Zad8

#Zad9

print(f"{round(nump.average(T), 1)}")
