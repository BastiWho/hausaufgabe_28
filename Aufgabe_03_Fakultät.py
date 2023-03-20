n = int(input("Bitte gib eine Zahl ein, die Fakultiert werden soll "))
f = 1
for i in range(1, n + 1):
    f *= i
print("Die Fakultät ist: ",f)