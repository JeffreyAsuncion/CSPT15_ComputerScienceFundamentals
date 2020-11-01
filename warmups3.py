"""
Example One
"""
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = my_list1
# How would you verify that my_list1 and my_list2 have the same identity?
print(my_list1 is my_list2)

my_list1.append(7)
# Check if my_list1 and my_list2 still have the same identity.
# If they do, why is that?
print(my_list1 is my_list2)



"""
Example Two
"""
my_text1 = "Lambda School"
my_text2 = my_text1
# How would you verify that my_text1 and my_text2 have the same identity?
print(my_text1 is my_text2)

my_text1 += " is awesome!"
# Check if my_text1 and my_text2 still have the same identity?
print(my_text1 is my_text2)
# If they do not, why is that?
## Strings are immutable

# Now check if my_text1 and my_text2 have the same value?
print(my_text1 == my_text2)
# Do they? Explain why or why not.
## Not, immutable


"""
Example Three
"""
# Initialize a list and assign to produce
produce = ["Apple", "Banana", "Carrot"]
# Initialize a tuple and include a reference to the produce list in the tuple
store = ("Bill's Grocery", produce)
print(id(store))
# Add a new item to the produce list
produce.append("Dragonfruit")
print(id(store))

# Did you notice that the identity of store remained the same?
# But I thought if you changed a mutable object, a new object would
# be created in memory? Why did that not occur here?
## the tuple become muttable because the list is mutable