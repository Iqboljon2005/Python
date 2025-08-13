# 1

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("Third fruit:", fruits[2])


# 2

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)




# 3 

numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("First, middle, last:", new_list)



# 4 

movies = ["Inception", "Titanic", "Avatar", "Interstellar", "Gladiator"]
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)



# 5

cities = ["London", "New York", "Paris", "Tokyo", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")



# 6 

nums = [1, 2, 3, 4, 5]
duplicated = nums * 2
print("Duplicated list:", duplicated)


# 7 

swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("After swapping:", swap_list)


# 8 

tuple_nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice (3 to 7):", tuple_nums[3:8])


# 9 

colors = ["blue", "red", "blue", "green", "blue"]
print("Blue appears:", colors.count("blue"), "times")


# 10 

animals = ("cat", "dog", "lion", "tiger")
print("Index of lion:", animals.index("lion"))


# 11

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
merged_tuple = tup1 + tup2
print("Merged tuple:", merged_tuple)


# 12

sample_list = [1, 2, 3, 4]
sample_tuple = (5, 6, 7)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))


# 13

tuple_to_list = (10, 20, 30, 40, 50)
converted_list = list(tuple_to_list)
print("Converted list:", converted_list)



# 14 

num_tuple = (15, 8, 22, 5, 17)
print("Max:", max(num_tuple))
print("Min:", min(num_tuple))


# 15

words_tuple = ("one", "two", "three")
print("Reversed tuple:", words_tuple[::-1])
