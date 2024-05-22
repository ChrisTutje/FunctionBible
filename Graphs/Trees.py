class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, parent_value, new_value):
        parent_node = self.search_node(parent_value)
        if parent_node:
            new_node = TreeNode(new_value)
            parent_node.children.append(new_node)
        else:
            print("Parent node is not available in the tree.")

    def search_node(self, value):
        return self._search_node_recursive(self.root, value)

    def _search_node_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found_node = self._search_node_recursive(child, value)
            if found_node:
                return found_node
        return None

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return None
        node.children = [self._delete_recursive(child, value) for child in node.children]
        return node
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def preorderTraversal(root):
    if root:
        print(root.value, end= " ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)
        
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.value, end = " ")
        inorderTraversal(root.right)
        
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        print(root.right)
        postorderTraversal(root.value, end = " ")

            
            
    
        
    
    
