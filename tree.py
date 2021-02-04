# A O(n) program for construction of BST from preorder traversal

INT_MIN = float("-infinity")
INT_MAX = float("infinity")
preIndex=0
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def incrementPreIndex():
    global preIndex
    preIndex+=1

def constructTreeUtil(pre,key,min_,max_,size):
    global preIndex
    if (min_>max_ or preIndex>=size):
        return None
    root=None
    if key>min_ and key<max_:
        root = Node(key)
        # print(root)
        incrementPreIndex()
        if (preIndex<size):
            root.left = constructTreeUtil(pre,pre[preIndex],min_,key,size)
        if (preIndex<size):
            root.right=constructTreeUtil(pre,pre[preIndex],key,max_,size)
    # print(root)
    return root    

def constructTree(pre):
    size=len(pre)
    global preIndex
    return constructTreeUtil(pre,pre[preIndex],INT_MIN,INT_MAX,size)

def PrintInOrder(node):
    if node:
        PrintInOrder(node.left)
        print(node.data,end=" ")
        PrintInOrder(node.right)

# def search(x,node):
#     if node is None :
#         return None 
#     elif node.data==x:
#         return node
#     elif node.data > x: 
#         return search(root.left,x) 
#     else:
#         return search(node.right,x)

def search(value,x):
    while x is not None:
        if value < x.data :
            x = x.left
        elif value > x.data:
            x = x.right
        else:
            return x.data
    return None


def insert(x,node):
    if node is None:
        y= Node(x)
        print(y,y.data)
        return y
    else:
        if node.data==x:
            return node
        elif node.data>x:
             node.left= insert(x,node.left)
        else:
            node.right = insert(x,node.right)
    return node


# Driver code
pre = [10, 5, 1, 7, 40, 50]

# Function call
root = constructTree(pre)
print ("Inorder traversal of the constructed tree: ")
PrintInOrder(root)
# print(search(40,root))
# if 4==search(4,root):
#     print("yess")
# else:
#     print()
#     print(search(40,root).data)


k=insert(44,root)
# print(k.data,k.left,k.right)
print(search(18,root))
PrintInOrder(root)