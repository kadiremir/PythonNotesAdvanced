"""2025, Kadir Emir, https://github.com/kadiremir

In this file, we explain the relationship between hashable and mutable data types in Python.

The following table shows which data types are hashable and which are mutable:

+---------------------+---------------------+
| Hashable (Immutable)| Non-Hashable (Mutable) |
+---------------------+---------------------+
| Strings             | Lists/Arrays         |
| Integers            | Dictionaries         |
| Tuples              | Sets                |
+---------------------+---------------------+

Hashable data types are immutable and can be used as keys in dictionaries or elements in sets.
Because they are immutable, their hash value does not change, which makes them suitable for use in hash tables.

Non-hashable data types are mutable and cannot be used as keys in dictionaries or elements in sets.
Because they are mutable, their hash value can change, which makes them unsuitable for use in hash tables.

Note that this convention and scheme is Python-specific and may vary in other programming languages.

####################################################################################################

Lets see what happens when we check an item is in a list or a set.
Consider we have a list of 1000 items and a set of 1000 items.


    For the list, we have to check each item one by one.
    So the time complexity is O(n).

    For the set, we can use a hash table to check if the item is in the set.
    The time complexity is O(1) on average.
    This is because hash tables have constant time complexity for lookups, insertions, and deletions.
"""
