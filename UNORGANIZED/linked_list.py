class Node:
    """This class creates a node"""
    def __init__(self, value):
        """..."""
        self.value = value
        self.next = None


class LinkedList:
    """This class creates a linked list"""
    def __init__(self, value):
        """..."""
        # Create a new (first) node of the linked list
        new_node = Node(value)
        # Assign the head and tail to the new and the only node
        self.head = new_node
        self.tail = new_node
        # Assign the length of the linked list
        self.length = 1

    def print_list(self):
        """Prints the linked list."""
        # Complexity: O(n)
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        """Adds a new node to the end of the linked list."""
        # Complexity: O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        """Removes and returns the last element of the linked list."""
        # Complexity: O(n)
        if self.length == 0:
            print("Nothing to be deleted.")
            return None  # List is empty; nothing to remove.

        tail_original = self.tail

        if self.length == 1:
            # If there's only one element, reset head and tail to None.
            self.head = None
            self.tail = None

        elif self.length == 2:
            # If there are two elements, reset tail to head and remove the second node.
            self.tail = self.head
            self.head.next = None

        else:
            # General case: more than two elements.
            node = self.head
            while node.next != self.tail:  # Find the second-last node.
                node = node.next
            node.next = None  # Disconnect the last node.
            self.tail = node  # Update the tail to the second-last node.

        self.length -= 1  # Decrement the length of the list.
        print(f"Deleting the current tail node: {tail_original}")
        return tail_original

    def prepend(self, value):
        """Adds a new node to the beginning of the linked list."""
        # Complexity: O(1)
        new_node = Node(value)
        print(f"Adding the new node (as head) {new_node}")
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node

    def pop_first(self):
        """Removes and returns the first element of the linked list."""
        # Complexity: O(1)
        if self.length == 0:
            print("Nothing to be popped, since LinkedList is empty.")
            return None

        current_head = self.head  # Save the current head for returning.

        if self.length == 1:
            print(f"There is only 1 node, and deleting it: {current_head}")
            self.head = None
            self.tail = None
        else:
            print(f"Deleting the first node (head): {current_head}")
            node = self.head.next
            self.head = node

        self.length -= 1

        return current_head

    def get(self, index):
        """Returns the node at the given index."""
        # Complexity: O(n)
        if index < 0 or index >= self.length:
            raise ValueError(f"Invalid index {index}. LinkedList has {self.length} nodes.")

        if self.length == 0:
            return None

        node = self.head

        for _ in range(index):
            node = node.next

        return node

    def set_value(self, index, value):
        expected_node = self.get(index)
        if expected_node:
            expected_node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        expected_node = self.get(index-1)
        expected_node_next_before_changing = expected_node.next
        new_node = Node(value)
        new_node.next = expected_node_next_before_changing
        expected_node.next = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(10)
print(f"The length is: {my_linked_list.length}")
print(f"The head of my linked list is {my_linked_list.head.value}")  # 10
my_linked_list.append(20)
print(f"The length is now: {my_linked_list.length}")
my_linked_list.print_list()

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
