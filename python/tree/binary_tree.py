class Node:

    def __init__(self, _val):
        self._val = _val
        self._left = None
        self._right = None

    def get_value(self):
        return self._val

    def get_left_node(self):
        return self._left

    def get_right_node(self):
        return self._right

    def set_left_node(self, node):
        self._left = node

    def set_right_node(self, node):
        self._right = node


def dfs_array(root: Node):
    result = []
    stack = [root]

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node is not None:
            stack.append(current_node.get_right_node())
            stack.append(current_node.get_left_node())
            result.append(current_node.get_value())

    return result


def dfs_recursion(root: Node):
    current_node = root

    if current_node is not None:
        left_value = dfs_recursion(current_node.get_left_node())
        right_value = dfs_recursion(current_node.get_right_node())

        return [current_node.get_value(), *left_value, *right_value]

    return []
