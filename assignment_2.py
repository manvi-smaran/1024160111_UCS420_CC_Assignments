roll_number = "1024160111"
L = [int(digit) * 10 for digit in roll_number]
print(L)

L.append(100)  # Appending 100 to the list
print(L)
L.insert(5, 50)  # Inserting 50 at index 5
print(L)

L.pop()  # Removing the last element from the list
print(L)

L.remove(10)
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

print(L[:3])
print(L[7:])

avg = sum(L) / len(L)
LQ = [x for x in L if x > avg]
print("Average:", avg)
print("Elements greater than average:", LQ)

#-----------------------------------------------
scores = tuple(L[:8])  # Converting the list to a tuple
print("Scores:", list(scores))

# Find highest score and its index in the tuple
max_score = max(scores)
max_index = scores.index(max_score)
print("Highest score:", max_score)
print("Index of highest score:", max_index)

# Find lowest score and how many times it appears
min_score = min(scores)
min_count = scores.count(min_score)
print("Lowest score:", min_score)
print("Count of lowest score:", min_count)

print("Scores in reverse order:", list(scores[::-1])) ## tuples are immutable, so we cannot sort them in place. Instead, we can create a new sorted list from the tuple.

number = int(input("Enter a number to check if it is present in the scores: "))
if number in scores:
    print(f"{number} is present in the scores.")
else:
    print(f"{number} is not present in the scores.")

# scores[1]=100

first_score, second_score,* remaining_scores = scores

#-----------------------------------------------
set_A ={int(digit)*7 for digit in roll_number[:8]}
set_B ={int(digit)*9 for digit in roll_number[:8]}
print("Set A:", set_A)
print("Set B:", set_B)

set_C = set_A.union(set_B)
print("Set C (Union of A and B):", set_C)
set_D = set_A.intersection(set_B)
print("Set D (Intersection of A and B):", set_D)
set_E = set_A.difference(set_B)
print("Set E (Difference of A and B):", set_E)
set_F = set_B.difference(set_A)
print("Set F (Difference of B and A):", set_F)
set_G = set_A.symmetric_difference(set_B)
print("Set G (Symmetric Difference of A and B):", set_G)
set_H = set_A.issubset(set_B)
print("Is Set A a subset of Set B?", set_H)
set_I = set_B.issuperset(set_A)
print("Is Set B a superset of Set A?", set_I)

X = int(input("Enter a value X to remove from Set A: "))
set_A.discard(X)
print(f"Set A after discarding {X}:", set_A)
# discard() is safer than remove() because it does nothing if the element is absent, avoiding a KeyError.

my_dict = {
    "name": "Alice",
    "roll_no": "1024160111",
    "branch": "ECE",
    "age": 20,
    "city": "Springfield"
}
my_dict["location"] = my_dict.pop("city")
my_dict["cgpa"] = 9.1
my_dict["age"] += 1

dict_with_pop = my_dict.copy()
removed_branch = dict_with_pop.pop("branch")
print("Removed branch with pop:", removed_branch)

dict_with_del = my_dict.copy()
del dict_with_del["branch"]
print("Dictionary after del branch:", dict_with_del)
print("pop returns the removed value, del does not return anything")

for key, value in my_dict.items():
    print(f"{key} → {value}")

if "email" in my_dict:
    print("email:", my_dict["email"])
else:
    print("email key not found")

friend_dict = {
    "name": "Bob",
    "roll_no": "2024250222",
    "branch": "ME",
    "age": 21,
    "city": "Metropolis"
}
merged_dict = {**my_dict, **friend_dict}
print("Merged dict:", merged_dict)
print("When keys overlap, the second dictionary's values win")

string_values_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("String-only dictionary:", string_values_dict)
