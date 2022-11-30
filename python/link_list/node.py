class Node:
    def __init__(self, value):
        self.head = None
        self.value = value
        self.next_node = None

    def get_node(self, value):
        if self.head is None:
            return None

        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node

        return None

    def add_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def remove_head(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next_node

    def get_value(self):
        return self.value

