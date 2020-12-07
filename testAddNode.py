import matplotlib.pyplot as plt
import numpy as np

def classifier(item):

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
    fashion_clothing = ["fashion clothing", "gucci", "supreme", "jewelery", "rolex", "louis vitton", "cartier", "chanel"]
    healthcare = ["healthcare", "medicine","primary care", "dental care", "specialty care", "urgent care", "medication", "medical devices",
                  "support", "nursing"]
    insurance = ["insurance","health insurance", "homeowner's insurance", "car insurance", "life insurance", "disability insurance"]
    householdItems = ["household items", "toiletries", "laundry detergent", "dishwasher detergent", "cleaning supplies", "tools"]
    personal = ["personal", "memberships", "haircut", "salon", "cosmetics", "babysitter", "birthday", "anniversary", "holiday",
                "wedding"]
    loans = ["personal loan", "student loan", "credit card"]
    education = ["education","textbooks", "student fees", "lab fees", "school supplies", "clubs", "conferences", "books"]
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
    elif(name in fashion_clothing):
        category = "fashion clothing"
    elif(name in healthcare):
        category = "healthcare"
    elif(name in insurance):
        category = "insurance"
    elif(name in householdItems):
        category = "household items"
    elif(name in personal):
        category = "personal"
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
    if (category == "personal" or category == "entertainment" or category == "fashion clothing"):
        levelOfNeed = "luxury"

#returns an array of the category and sub category:
    return [category, levelOfNeed]

class item:
#sets up item object with name, cost, level of need(luxury or necessity), and category
    def __init__(self, name=None, cost=None):
        self.name = name
        self.cost = cost
        self.levelOfNeed = classifier(self)[1]
        self.category = classifier(self)[0]

class monthly_expenses:
#sets up monthly expense object (part of tree)
    def __init__(self, l, date_num):
        self.l = l
        self.parent = None
        self.right_child = None
        self.left_child = None
        self.balance_factor = 0
        self.height = 1
        self. date_num = date_num
#gets total cost of all items or services purchased within a month
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

    # private function to recursively check for the new monthly expense node to be placed
    def __add_monthly_expense(self, current_node, l):

        #inserts monthly total cost to either the left or right based on relative value of the root:

        #if monthly total is less than root:
        if l.total_cost() < current_node.total_cost():
            #if no root is present, create one
            if current_node.left_child == None:
                current_node.left_child = l
                current_node.left_child.parent = current_node
                self.update_balance(current_node)
                self.check_balance(current_node)
            else:
                self.__add_monthly_expense(current_node.left_child, l)
        elif l.total_cost() > current_node.total_cost():
            #if monthly total is greater than root (if exists)
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

    #the following functions are for balancing the tree
    def right_rotation(self, node):

        A = node
        B = node.left_child
        BL = B.right_child
        C = B.left_child

        newParent = B
        A.left_child = BL

        #performs right rotation by first checking if left and parent node exists
        if BL != None:
            BL.parent = A

        B.parent = A.parent

        if A.parent == None:
            self.root = B
        #performs rotation
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.right_child = A
        A.parent = B

        self.update_balance(B)
        self.update_balance(A)

#performs left rotation
    def left_rotation(self, node):
#Setting the poper placment of nodes
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
        #set up parent nodes if created correctly
        #if parents exist, perform rotation as is:
        else:
            if A.parent.left_child == A:
                A.parent.left_child = B
            else:
                A.parent.right_child = B

        B.left_child = A
        A.parent = B
#Updating the tree
        self.update_balance(B)
        self.update_balance(A)


    def get_LON_items(self):
        if self.root != None:
            items = []
            self.__get_LON_items(self.root, items)
        overall_list = []
        monthly_necessity = []
        monthly_luxury = []
        necessities = []
        luxuries = []
        for item in items:
            for expense in item.l:
                if expense.levelOfNeed == "necessity":
                    monthly_necessity.append(expense)
                else:
                    monthly_luxury.append(expense)
            necessities.append(monthly_necessity)
            luxuries.append(monthly_luxury)
            monthly_luxury = []
            monthly_necessity = []
        return necessities, luxuries


    def __get_LON_items(self, current_node, items):
        if current_node != None:
            self.__get_LON_items(current_node.left_child, items)
            items.append(current_node)
            self.__get_LON_items(current_node.right_child, items)

    def printTree(self, root):
        if root != None:
            self.printTree(root.left_child)
            if (root.l != []):
                print(len(root.l))
            else:
                print(None)
            self.printTree(root.right_child)

#sets up graph for a specifc month's expenses : either for necessity or for luxuries
def graph_levelOfNeed(monthly_list, necessity_list=False):

    #set up basic variable values
    housing, transportation, food, utilities, clothing, healthcare, insurance, household_items, loans, education, savings, miscellaneous = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    entertainment, personal, fashion_clothing = 0, 0, 0

    for item_node in monthly_list:
        #adds categories for the graphs to be displayed on x-axis
        if necessity_list:
            if item_node.category == "housing":
                housing += item_node.cost
            elif item_node.category == "transportation":
                transportation += item_node.cost
            elif item_node.category == "food":
                food += item_node.cost
            elif item_node.category == "utilities":
                utilities += item_node.cost
            elif item_node.category == "clothing":
                clothing += item_node.cost
            elif item_node.category == "healthcare":
                healthcare += item_node.cost
            elif item_node.category == "insurance":
                insurance += item_node.cost
            elif item_node.category == "household items":
                household_items += item_node.cost
            elif item_node.category == "loans":
                household_items += item_node.cost
            elif item_node.category == "education":
                education += item_node.cost
            elif item_node.category == "savings":
                savings += item_node.cost
            else:
                miscellaneous += item_node.cost
        else:
            if item_node.category == "entertainment":
                entertainment += item_node.cost
            elif item_node.category == "personal":
                personal += item_node.cost
            else:
                fashion_clothing += item_node.cost

    if necessity_list:
        expenses = (housing, transportation, food, utilities, clothing, healthcare, insurance, household_items, loans, education, savings, miscellaneous)
    else:
        expenses = (entertainment, personal, fashion_clothing)

    if necessity_list:
        categories = ["housing", "transportation", "food", "utilities", "clothing", "healthcare", "insurance", "household items", "loans", "education", "savings", "miscellaneous"]
    else:
        categories = ["entertainment", "personal", "fashion clothing"]

    y_pos = np.arange(len(categories))
    plt.bar(y_pos, expenses, align='center', alpha=0.5)
    plt.xticks(y_pos, categories)
    plt.ylabel('Total Cost ($)')
    plt.title('Expenditure bar graph')

    plt.show()


# sample_list = monthly_expenses([item('utilities', 1.25),
#                                 item('electricity', 60),
#                                 item('books', 15.24)
#                                 ])
#
# sample_list1 = monthly_expenses([item('games', 100),
#                                  item('movies', 1000000),
#                                  item('water', 2.5)
#                                  ])
#
# test_tree = expense_tree()
# test_tree.add_monthly_expense(sample_list)
# test_tree.add_monthly_expense(sample_list1)
#
# test_necessity = test_tree.get_LON_items()[0][1]
# graph_levelOfNeed(test_necessity, False)

