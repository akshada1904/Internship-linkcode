n = int(input("Enter a number: "))
temp = n
count = len(str(n))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit ** count
    n = n // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")