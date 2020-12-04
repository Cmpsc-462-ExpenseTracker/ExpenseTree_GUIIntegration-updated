def classifier(item):  # Himani: commenting outline

    # store off cost and name from item for classification use

    name = item.name
    category = "" #type of category
    levelOfNeed = "necessity" #necessity (default) or luxury

    # create a list of keywords for each type of personal expense:
    #perhaps the GUI can have the user select one of these words when entering their expense
    housing = ["housing", "mortgage", "rent", "property tax", "repairs", "housing fees"]
    transportation = ["transportation", "car mortgage", "bus", "train", "gas", "tires", "repairs", "parking fees", "maintenance",
                      "warranty", "uber", "taxi"]
    food = ["food", "groceries", "restaurants", "pet food", "snacks"]
    utilities = ["utilities","electricity", "water", "garbage", "sewage", "heating", "cooling", "AC", "mobile network", "internet",
                 "cable", "laundry"]
    clothing = ["clothing","professional attire", "formal wear", "casual wear", "shoes", "accessories"]
    healthcare = ["healthcare", "medicine","primary care", "dental care", "specialty care", "urgent care", "medication", "medical devices",
                  "support", "nursing"]
    insurance = ["insurance","health insurance", "homeowner's insurance", "car insurance", "life insurance", "disability insurance"]
    householdItems = ["household items", "toiletries", "laundry detergent", "dishwasher detergent", "cleaning supplies", "tools"]
    personal = ["personal", "memberships", "haircut", "salon", "cosmetics", "babysitter", "birthday", "anniversary", "holiday",
                "wedding"]
    loans = ["personal loan", "student loan", "credit card"]
    education = ["education","textbooks", "student fees", "lab fees", "school supplies", "clubs", "conferences"]
    savings = ["savings", "emergency", "long-term savings"]
    entertainment = ["entertainment", "games", "movie", "concerts", "party", "vacations", "alcohol", "subscription", "sport",
                    "social events"]

#check if the item name fits in one of these categories
    if (name in housing):
        category = "housing"
    elif(name in transportation):
        category = "transportation"
    elif(name in food):
        category = "food"
    elif(name in utilities):
        category = "utilities"
    elif(name in clothing):
        category = "clothing"
    elif(name in healthcare):
        category = "healthcare"
    elif(name in insurance):
        category = "insurance"
    elif(name in householdItems):
        category = "household items"
    elif(name in personal):
        category = personal
    elif(name in loans):
        category = "loans"
    elif(name in education):
        category = "education"
    elif(name in savings):
        category = "savings"
    elif(name in entertainment):
        category = "entertainment"
    else:
        category = "miscellaneous" #if category isn't identified

#luxury if personal, entertainment (may need adjusting - perhaps add functions to tweak definition of "luxury" for each user using input)
    if (category == "personal" or category == "entertainment"):
        levelOfNeed = "luxury"

#returns an array of the category and sub category:
    return [category, levelOfNeed]

class item:

    def __init__(self, name, cost):
        self.name = name
        self.levelOfNeed = classifier(self)[1]
        self.cost = cost
        self.category = classifier(self)[0]

class monthly_expenses:

    def __init__(self, l):
        self.l = l
        self.parent = None
        self.right_child = None
        self.left_child = None
        self.balance_factor = 0
        self.height = 1

    def total_cost(self):
        total = 0
        for each_expense in self.l:
            total += each_expense.cost
        return total


class expense_tree:

    def __init__(self):
        self.root = None

    # function to add individual monthly expenses
    def add_monthly_expense(self, l):
        if not self.root:
            self.root = l
        else:
            self.__add_monthly_expense(self.root, l)

    # IGNORE
    # private function to recursively check for the new monthly expense node to be placed
    def __add_monthly_expense(self, current_node, l):

        if l.total_cost() < current_node.total_cost():
            if current_node.left_child == None:
                current_node.left_child = l
                current_node.left_child.parent = current_node
                self.update_balance(current_node)
                self.check_balance(current_node)
            else:
                self.__add_monthly_expense(current_node.left_child, l)
        elif l.total_cost() > current_node.total_cost():
            if current_node.right_child == None:
                current_node.right_child = l
                current_node.right_child.parent = current_node
                self.update_balance(current_node)
                self.check_balance(current_node)
            else:
                self.__add_monthly_expense(current_node.right_child, l)

    # function to check balance of the expense tree
    def check_balance(self, current_node):
        if current_node == None:
            return
        bF = current_node.balance_factor
        if abs(bF) > 1:
            self.rebalance(current_node)
            return
        self.check_balance(current_node.parent)

    # function to update the balance factor
    def update_balance(self, current_node):
        if current_node == None:
            return
        current_node.height = 1 + max(self.get_height(current_node.left_child), self.get_height(current_node.right_child))
        current_node.balance_factor = self.get_height(current_node.left_child) - self.get_height(current_node.right_child)
        self.update_balance(current_node.parent)

    # function to access the height of a node
    def get_height(self, node):
        if node == None:
            return 0
        return node.height

    # function to rebalance the expense tree
    def rebalance(self, current_node):
        if current_node.balance_factor < 0:
            if current_node.right_child.balance_factor > 0:
                self.right_rotation(current_node.right_child)
                self.left_rotation(current_node)
            else:
                self.left_rotation(current_node)
        elif current_node.balance_factor > 0:
            if current_node.left_child.balance_factor < 0:
                self.left_rotation(current_node.left_child)
                self.right_rotation(current_node)
            else:
                self.right_rotation(current_node)

    def right_rotation(self, node):

        A = node
        B = node.left_child
        BL = B.right_child
        C = B.left_child

        newParent = B
        A.left_child = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.right_child = A
        A.parent = B

        self.update_balance(B)
        self.update_balance(A)

    def left_rotation(self, node):

        A = node
        B = node.right_child
        BL = B.left_child
        C = B.right_child

        newParent = B
        A.right_child = BL

        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.left_child = A
        A.parent = B

        self.update_balance(B)
        self.update_balance(A)

class BST:

    def __init__(self):
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def bstInsert(self, val, currentNode):
        if val < currentNode.val: #if new value is less than current node's value
            if currentNode.leftChild: #if left child node exists,
                self.bstInsert(val, currentNode.leftChild) #recursive call for the left child
            else:
                currentNode.leftChild = BSTNode(val, parent=currentNode)
                # print("current left child of " + str(currentNode.val) + ": " + str(currentNode.leftChild.val))
        else:
            if currentNode.rightChild:
                self.bstInsert(val, currentNode.rightChild)
            else:
                currentNode.rightChild = BSTNode(val, parent=currentNode)
                # print("current right child of "  +  str(currentNode.val) + ": "+ str(currentNode.rightChild.val))

#Himani: BST Class
class BSTNode:
    def __init__(self, val, left=None, right=None, parent=None):
        # print("--------------")
        # print("node value: " + str(val))
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        # BST node has a value, left and right children, and parent


def getHeight(node):
    if (node is None or node.parent is None):
        return 0
    else:
        return 1 + getHeight(node.parent)
    # recursively adds height for each parent reached from child to root

def build_bst(list):
    list = remove_duplicates(list)  # remove duplicates
    count = 0
    BSTree = BST()  # creates basic BST with no root value yet
    rootNode = BSTNode(list[0].cost)
    BSTree.root = rootNode
    for x in list[1:]:
        BSTree.bstInsert(x, rootNode) #creates root node from first in list
        #then inserts the next elements based on that root
    return BSTree

def remove_duplicates(list):
    newList = []
    length = len(list)  # for loop length
    for x in range (0, length):  # last element at length -1
        if (list[x] not in newList): #current element isn't in blank array, add it
            newList.append(list[x])

    return newList #returns a list without duplicates

def findMin(binTree):
    if (binTree == None):
        return float('inf') #can't use a specific number - minimum will get thrown off

    min = binTree.value  # initial minimum is root
    leftMin = findMin(binTree.leftChild)  # finds minimum on left side (recursively)
    #print("leftMin: "+ str(leftMin))
    rightMin = findMin(binTree.rightChild)  # finds min on right side (recursively)

    if (leftMin < min): #if left's minimum is smaller than root' value, min is now leftMin
        min = leftMin
    elif(rightMin < min): #if rightMin < min of left side and root, min is now rightMin
        min = rightMin

    return min
def findMax(binTree):
    if (binTree == None):
        return float('-inf') #can't use a specific number - maximum will get thrown off

    max = binTree.value  # initial max is root
    leftMax = findMax(binTree.leftChild)  # finds maximum on left side (recursively)
    #print("leftMin: "+ str(leftMin))
    rightMax = findMax(binTree.rightChild)  # finds max on right side (recursively)

    if (leftMax > max): #if left's maximum is smaller than root' value, max is now leftMax
        max = leftMax
    elif(rightMax > max): #if rightMax < max of left side and root, max is now rightMax
        max = rightMax

    return max

def printBST(BST):
    print("BST size: " + str(BST.length()))
    for x in range(0, BST.length()):
        print(str(x) + ": " + str(BST[x])) #prints all values by key in order

def preorderBST(bstRoot): #uses recursion to traverse the BST : root, left, then right
    if bstRoot != None:
        root = bstRoot
        print("root: " + str(root.val)) #prints root value
        print("------")
        if bstRoot.leftChild: #prints value and height of the current root's left child
            print("current left child of " + str(bstRoot.val) + ": " + str(bstRoot.leftChild.val))
            level = getHeight(bstRoot)
            print("LEFT CHILD HEIGHT:" + str(level))
            preorderBST(bstRoot.leftChild)
        if (bstRoot.rightChild): #prints value and height of the current root's right child
            level = getHeight(bstRoot)
            print("current right child of " + str(bstRoot.val) + ": " + str(bstRoot.rightChild.val))
            print("RIGHT CHILD HEIGHT: " + str(level))
            preorderBST(bstRoot.rightChild)
    else:
        print("----")