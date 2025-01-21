# Basically a linked list is a dictionary with a key and a value. The key is the data and the value is the next node.

head = {
    "data": 10,
    "next": {
        "data": 20,
        "next": {
            "data": 30,
            "next": {
                "data": 40,
                "next": None
            }
        }
    }
}

# This is a definition of a linked list with 4 nodes. The head is the first node and the last node is None.
# For instance,

# to get the node value of the head:
print(head["data"])  # 10
# to get the next node of the head:
print(head["next"]["data"])  # 20
# to get the next node of the next node of the head:
print(head["next"]["next"]["data"])  # 30
# to get the tail node:
print(head["next"]["next"]["next"]["data"])
print()