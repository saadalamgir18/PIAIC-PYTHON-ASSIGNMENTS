# 1. Add two numbers
num1:float = float(input("enter first number? "))
num2:float = float(input("enter second number? "))
sum: float = num1 + num2
print("sum of two numbers is", sum)

# 2. Agreement Boot
animal: str = input("what's your favorite animal? ")
print(f"My favorite animal is also {animal}!") 

# 3. Fahrenheit to Celsius
fahrenheit:float = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature: {fahrenheit}F = {(fahrenheit - 32) * 5.0/9.0}C")

# 4. Triangle Perimeters
side1:float = float(input("Enter length of side 1? ")) 
side2:float = float(input("Enter length of side 2? "))
side3:float = float(input("Enter length of side 3? "))
print(f"The perimeter of the triangle: {side1 + side2 + side3}")

#5. Square Number

number:float = float(input("Type a number to see its square: "))
print(f"{number} squared is {number**2}")

#6 Delete a number
numbers = [1, 2, 3, 4, 5]
print("befor: ",numbers)
numbers.remove(3)
print("After: ",numbers)

# 7 Creating a list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 8. Pop method

items = [10, 20, 30, 40]
#anser:
# if we use pop method without arguments the last item of the list which is 40 will be removed

# 9.  Index Method
colors = ['red', 'blue', 'green', 'yellow']

print(colors.index('green'))  # Output: 2 (index of 'green')

# Challenge Questions


# 10. Get last element
def get_last_element(lst):
    print(lst[-1])
get_last_element([1,2,3,4,5])

# 11. Get a List

alist = []
while True:
    user_input = input("Enter a number (or 'Enter' to quit): ")
    
    if user_input.lower() == '':
        print(alist)
        break
    alist.append(int(user_input))
    
