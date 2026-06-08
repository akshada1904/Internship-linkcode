#print odd index no
s = input("Enter a string: ")

for i in range(len(s)):
    if i % 2 != 0:
        print(s[i], end="")

#print vowel from string
s = input("Enter a string: ")

for ch in s:
    if ch in "aeiouAEIOU":
        print(ch, end=" ")

#count even &odd position characters
s = input("Enter a string: ")

even = 0
odd = 0

for i in range(len(s)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even characters =", even)
print("Odd characters =", odd)

#reverse string without slicing
s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reverse =", rev)

#palindrome string
s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")