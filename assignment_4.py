
numbs_list : [int] = []
name: str = input("Enter your name: ")
num1: int = int(input("Enter your first favorite number: "))
numbs_list.append(num1)
num2: int = int(input("Enter your second favorite number: "))
numbs_list.append(num2)
num3: int = int(input("Enter your third favorite number: "))
numbs_list.append(num3)



print(f"Hello, {name}! Let's explore your favorite numbers:")
tuples_list : [(int, str)] = []
for num in numbs_list:
    tuples_list.append((num, "even" if num % 2 == 0 else "odd"))
    
for num_tuple in tuples_list:
    print(f"The number {num_tuple[0]} is {num_tuple[1]}.")  

for num_tuple in tuples_list:
    print(f"The number {num_tuple[0]} and its square: ({num_tuple[0]}, {num_tuple[0]**2})")


sum: int = num1 + num2 + num3
print(f"Amazing! The sum of your favorite numbers is: {sum}")

if (sum > 1 or sum == 2) and sum % 2 != 0:
    print(f"Wow, {sum} is a prime number!")
