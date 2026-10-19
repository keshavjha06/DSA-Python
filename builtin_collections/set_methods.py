# A set doesn't accept duplicates and doesn't keep insertion order.
# Elements are found using their hash codes.

hash_set = set()
hash_set.add(10)
hash_set.add(20)
hash_set.add(30)
hash_set.add(40)
hash_set.add(50)
hash_set.add(60)
print(hash_set)
print(10 in hash_set)  # True
print(100 in hash_set)  # False
hash_set.remove(10)
print(hash_set)
hash_set.discard(100)  # discard() doesn't raise an error if missing
print(hash_set)
hash_set.clear()
print(hash_set)  # set()
print(len(hash_set) == 0)  # True

# Python has no LinkedHashSet; a dict's keys keep insertion order
linked_hash_set = {}
linked_hash_set[10] = None
linked_hash_set[20] = None
linked_hash_set[30] = None
linked_hash_set[40] = None
linked_hash_set[50] = None
linked_hash_set[60] = None
print(list(linked_hash_set))  # [10, 20, 30, 40, 50, 60]
# sorted order (like TreeSet): sorted(hash_set)

# set -> O(1) lookup
# TreeSet (BST) -> O(log n)
