# 1

txt = 'MsaatmiazD'

car = txt[::2] 

print(car)



# 2 

txt = "I'am John. I am from London"

place = txt.split("from ")[1]

print(place)


# 3 

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)


# 4


word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")


# 5 

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("The third fruit is:", fruits[2])


# 6 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)



# 7

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

new_list = [first, middle, last]

print("New list:", new_list)



# 8 

cities = ["London", "New York", "Paris", "Tokyo", "Berlin"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")



# 9 

numbers = [1, 2, 3, 4, 5]

duplicated_list = numbers * 2

print("Duplicated list:", duplicated_list)


# 10

numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("After swapping:", numbers)
