#simple list print
fruits = ["Apple", "Mango", "Banana"]
print(fruits)

#access element
fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])
print(fruits[1])

#add element
fruits = ["Apple", "Mango"]
fruits.append("Banana")
print(fruits)

#remove element
fruits = ["Apple", "Mango", "Banana"]
fruits.remove("Mango")
print(fruits)

#length of list
numbers = [10, 20, 30, 40]
print(len(numbers))

#user input list
numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

print(numbers)

#sort list
numbers = [5, 2, 8, 1]

numbers.sort()
print(numbers)