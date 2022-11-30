from sort import bubble_sort
from tree.binary_tree import Node, dfs_array, dfs_recursion

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ====== Bubble Sort =======
    # print("Bubble Sort ======= ", bubble_sort.bubble_sort([5, 2, 4, 1, 2]))

    # ====== Binary tree traversal ======
    nodeA = Node('a')
    nodeB = Node('b')
    nodeC = Node('c')
    nodeD = Node('d')
    nodeE = Node('e')
    nodeF = Node('f')
    nodeG = Node('l')
    nodeH = Node('h')
    nodeI = Node('i')
    nodeK = Node('k')
    nodeL = Node('l')
    nodeM = Node('m')
    nodeN = Node('n')

    nodeA.set_left_node(nodeB)
    nodeA.set_right_node(nodeC)
    nodeB.set_left_node(nodeD)
    nodeB.set_right_node(nodeE)
    nodeC.set_left_node(nodeF)
    nodeC.set_right_node(nodeG)
    nodeD.set_left_node(nodeH)
    nodeD.set_right_node(nodeI)
    nodeE.set_left_node(nodeK)
    nodeE.set_right_node(nodeL)
    nodeF.set_left_node(nodeM)
    nodeF.set_right_node(nodeN)

    dfs_array_rs = dfs_array(nodeA)
    dfs_recursion_rs = dfs_recursion(nodeA)
    print("========= DFS ARRAY =========")
    print(dfs_array_rs)

    print("========= DFS RECURSION =========")
    print(dfs_recursion_rs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
