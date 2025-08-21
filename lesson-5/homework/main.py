# Task 1

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year ✅")
else:
    print(f"{year} is not a leap year ")



# Task 2

n = int(input("Enter a number: "))

if n % 2 == 1:  # odd
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# Task 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 2 != 0:   # if a is odd, make it even
    a += 1

evens = list(range(a, b + 1, 2))
print("Even numbers:", evens)
