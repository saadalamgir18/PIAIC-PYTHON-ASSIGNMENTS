# 1 Age Assignments Based on the Riddle
Anton: int = 21
Beth : int = Anton + 6
Chen: int = Beth + 20
Drew : int = Chen + Anton
Ethan: int = Chen

print("Anton is ", Anton)
print("Beth is ", Beth)
print("Chen is ", Chen)
print("Drew is ", Drew)
print("Ethan is ", Ethan)


# 2 Formatted String Interpolation
name:str = "Alice"
age:int = 30
city:str = "New York"

print(f"{name} is {age} years old and lives in {city}")


# 3 String Manipulation

s:str = "hElLo WoRlD"
print(s.capitalize())
print(s.upper())
print(s.lower())

# 4 Substring Search

s:str ="the quick brown fox jumps over the lazy dog"
print(f"index of 'fox' is {s.index('fox')}")
print(f"'the' appears {s.count('the')} times")


# 5 String Replacement

s:str ="I love programming in Python"
print(s.replace("Python", "Java"))


# 6 String Splitting and Joining

s:str ="apple,banana,cherry,dates"
slist = s.split(",")
print(slist)
print(" ".join(slist))


# 7 String Stripping and Justifying

s:str ="   Python is fun!   "
new_s : str = s.strip()
print(new_s)
print(new_s.rjust(20, "*"))
print(new_s.ljust(20, "*"))


# 8 Convert an integer to its binary representation

num:int = 45
print("Binary representation :",bin(num))

# 9 Calculate Powers of Numbers.
base:int = 3
exponent:int = 4
print("Power result:",base**exponent)

# 10 Round floating-point numbers

value:float = 12.34567
print("Rounded to nearest integer:", round(value))
print("Rounded to two decimal places:", round(value, 2))