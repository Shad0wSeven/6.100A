# Problem Set 4a
# Name: Ayush Nayak
# Collaborators: None
# Time spent: 0:15

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree_1 = Node(9, Node(6), Node(3, Node(7), Node(8)))
tree_2 = Node(7, Node(13, Node(15, Node(4), Node(6)), Node(5)), Node(2, Node(9), Node(11)))
tree_3 = Node(4, Node(9, Node(14), Node(25)), Node(17, Node(1), Node(8, Node(11), Node(6))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree == None:
        return -1
    else:
        return 1 + max(find_tree_height(tree.left), find_tree_height(tree.right))

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree compare_func: 
              a function that compares the child node value to the parent node value
            
            i.e. compare_func(child_value,parent_value) for a max heap would return False 
                 if child_value > parent_value and True otherwise
                 
                 compare_func(child_value,parent_value) for a min meap would return False 
                 if child_value < parent_value and True otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree == None:
        return True
    elif tree.left == None and tree.right == None:
        return True
    elif tree.left == None:
        return compare_func(tree.right.value, tree.value) and is_heap(tree.right, compare_func)
    elif tree.right == None:
        return compare_func(tree.left.value, tree.value) and is_heap(tree.left, compare_func)
    else:
        return compare_func(tree.left.value, tree.value) and is_heap(tree.left, compare_func) and compare_func(tree.right.value, tree.value) and is_heap(tree.right, compare_func)

if __name__ == '__main__':
    # # You can use this part for your own testing and debugging purposes.
    # # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass