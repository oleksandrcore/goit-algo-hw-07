class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_max_value(root):
    if root is None:
        return None
    
    while root.right:
        root = root.right
    
    return root.val

def find_min_value(root):
    if root is None:
        return None
    
    while root.left:
        root = root.left
    
    return root.val

def find_sum(root):
    if root is None:
        return 0
    
    return root.val + find_sum(root.left) + find_sum(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

print(f"Найбільше значення у дереві: {find_max_value(root)}")
print(f"Найменше значення у дереві: {find_min_value(root)}")
print(f"Сума всіх значень у дереві: {find_sum(root)}")