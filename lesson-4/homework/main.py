# ---------------- Dictionary Exercises ----------------


# 1

d = {2: 30, 1: 40, 4: 20, 3: 50}
asc = dict(sorted(d.items(), key=lambda item: item[1]))
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)



# 2

d2 = {0: 10, 1: 20}
d2[2] = 30
print("After adding key:", d2)



# 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated dictionary:", new_dict)



# 4

n = 5
squares = {x: x * x for x in range(1, n + 1)}
print("Squares (1 to n):", squares)



# 5

squares_15 = {x: x * x for x in range(1, 16)}
print("Squares (1 to 15):", squares_15)



# ---------------- Set Exercises ----------------


# 1

my_set = {1, 2, 3}
print("Created set:", my_set)



# 2

print("Iterating over set:")
for item in my_set:
    print(item)



# 3

my_set.add(4)
my_set.update([5, 6])
print("After adding members:", my_set)



# 4

my_set.remove(6)  # will throw error if not found
print("After removing 6:", my_set)



# 5

my_set.discard(10)  # won't throw error if not found
print("After discarding 10 (if present):", my_set)
