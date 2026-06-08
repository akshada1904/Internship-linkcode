#star pattern
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

#xox pattern
for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

#no triangle
num = 1

for i in range(1, 4):
    for j in range(i):
        print(num, end=" ")
    print()
    num += 2

#string pattern
ch = 'a'

for i in range(3, 0, -1):
    for j in range(i):
        print(ch, end="")
    print()
    ch = chr(ord(ch) + 1)


#reverse no pattern
for i in range(1, 4):
    num = 2 * i - 1
    for j in range(i):
        print(num, end=" ")
    print()

for i in range(2, 0, -1):
    num = 2 * i - 1
    for j in range(i):
        print(num, end=" ")
    print()