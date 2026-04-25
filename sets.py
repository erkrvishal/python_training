# Sets Example and Usage

# Declaring the Sets

# a = set() # Initialize an empty set
# a = {}
# a = {"a","b","c"} # Initialize set

# a = [1,1,2,3,3]
# print(set(a)) #Remove the duplicate values
# a.add(5) #Add a value to the existing set
# print(a)
# a.update([1,2,5,6])
# print(a)

# a.discard(3)
# print(a)
# a.remove(3)
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)

a = {1,2,3,4} #subset of b
b = {4,5,6,7} # Superset of a
# union() or |
#intersection() or &
# difference() or -
# symmetric_difference() or ^
# print(a | b)
# print(a & b)
# print(b - a)
# print(a^b)
# print(a.isdisjoint(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.intersection_update(b))
# print(a)
# print(b)
# print(a.difference_update(b))
# print(a)
# print(b)