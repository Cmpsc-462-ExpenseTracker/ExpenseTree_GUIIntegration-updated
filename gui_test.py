# Matt: this imports the expense tracker .py file
from testAddNode import *
# Matt: december is the monthly expenses
import matplotlib.pyplot as plt
import numpy as np

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

expense_tracker = expense_tree()
months = {1: [],  #these are the months that hold a list
          2: [],
          3: [],
          4: [],
          5: [],
          6: [],
          7: [],
          8: [],
          9: [],
          10: [],
          11: [],
          12: []}


#
# #(GUI button call) function to graph necessities or luxuries
# def show_expenditure_overview()


def Addexpense(): #Matt: Addexpense is used when the user adds an expense via GUI
    print('yes2')

    Date = EDate.get() # this is the data string box
    ItemName = Title.get() #item name string box
    ItemPrice = float(Expense.get()) #price string box
    ItemCategory = item(ItemName, ItemPrice).category #item category holds the inputed item cata gory

    data = [Date, ItemName, ItemPrice, ItemCategory]

    # sets up the key from the months dictionary
    # example: 1/12/20 --> January (1)

    month_num = Date[:2] #month_num has the first two characters of Date
    if '/' in month_num:
        month_num = int(Date[0])
    else:
        month_num = int(Date[:2]) #cast month_num as date int
    print("Month num", month_num)
    months[month_num].append(item(ItemName, ItemPrice)) #add item to specific month
    print("length ", len(months[month_num]))

    for key in months.keys():
        m_l = monthly_expenses(months[key])
        expense_tracker.add_monthly_expense(m_l)

    expense_tracker.printTree(expense_tracker.root)

    # print("Root of the expense tree", expense_tracker.root.l)
    #
    # print("Left Child of the root", expense_tracker.root.left_child)
    #
    # '''decemberMonth = december.monthly_expenses(decemberItem)
    # december.expense_tree.add_monthly_expense(decemberMonth, decemberItem)'''

    TVExpense.insert('', 'end', values=data)

def test_graph():

    plt.figure(1) #plots the figure 1
    plt.show() #displays the current plot

def create_GRAPH_display():

    def january(): #january button
        # the figure that will contain the plot
        fig = Figure(figsize=(5, 5), dpi=100)

        # adding the subplot
        plot1 = fig.add_subplot(111)

        categories = ["ye1", "ye2"]
        expenses = [2,3]

        y_pos = np.arange(len([categories]))
        plot1.bar

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=graph_GUI)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, graph_GUI)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    graph_GUI = Tk()

    graph_GUI.title('** Visual View of Expenditure **')
    graph_GUI.geometry('700x700')

    january_button = Button(master=graph_GUI, command=january, height=2, width=10, text="Plot")

    # january = ttk.Button(graph_GUI, text="January", command=january)
    # january.grid(row=2, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # february = ttk.Button(graph_GUI, text="February", command=None)
    # february.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # march = ttk.Button(graph_GUI, text="March", command=None)
    # march.grid(row=4, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # april = ttk.Button(graph_GUI, text="April", command=None)
    # april.grid(row=5, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # may = ttk.Button(graph_GUI, text="May", command=None)
    # may.grid(row=6, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # june = ttk.Button(graph_GUI, text="June", command=None)
    # june.grid(row=7, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # july = ttk.Button(graph_GUI, text="July", command=None)
    # july.grid(row=8, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # august = ttk.Button(graph_GUI, text="August", command=None)
    # august.grid(row=9, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # september = ttk.Button(graph_GUI, text="September", command=None)
    # september.grid(row=10, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # october = ttk.Button(graph_GUI, text="October", command=None)
    # october.grid(row=11, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # november = ttk.Button(graph_GUI, text="November", command=None)
    # november.grid(row=12, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)
    #
    # december = ttk.Button(graph_GUI, text="December", command=None)
    # december.grid(row=13, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    january_button.pack()
    # B.pack()
    graph_GUI.mainloop()
    # Tab = Notebook(graph_GUI)
    # F1 = Frame(Tab, width=500, height=500, bg="cyan")
    #
    # BFInewMonth = ttk.Button(F1, text='Visualize', command=create_GRAPH_display)
    # BFInewMonth.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)



# def New_Month():
#
#     print('yes1')
#     Addexpense()
#     # print(expense_tracker.get_LON_items()[0])

#
GUI = Tk()
GUI.title('** Expense Recorder **')
GUI.geometry('1000x600')
# Maximize windrow
# GUI. state ('zoomed')

Tab = Notebook(GUI)
F1 = Frame(Tab, width=500, height=500, bg="cyan")
Tab.add(F1, text='Expense')

Tab.pack(fill=BOTH, expand=1)
# Tab 1 (Expense)

# ==========Row 0 ===========================
LDate = ttk.Label(F1, text='Date', font=(None, 18))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

EDate = DateEntry(F1, width=19, background='blue', foreground='white', font=(None, 18))
EDate.grid(row=0, column=1, padx=5, pady=5)

# ==========Row 1 ===========================
LTitle = ttk.Label(F1, text='Title', font=(None, 18))
LTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')
Title = StringVar()
ETitle = ttk.Entry(F1, textvariable=Title, font=(None, 18))
ETitle.grid(row=1, column=1, padx=5, pady=5)
# ========== Row 2 =====================
LExpense = ttk.Label(F1, text='Expense', font=(None, 18))
LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

EExpense = ttk.Entry(F1, textvariable=Expense, font=(None, 18))
EExpense.grid(row=2, column=1, padx=5, pady=5)

# ========== Row 3 =====================
BFIadd = ttk.Button(F1, text='Add', command=Addexpense)
BFIadd.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ========== Row 3 =====================
BFInewMonth = ttk.Button(F1, text='Visualize', command=create_GRAPH_display)
BFInewMonth.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)


# ========= Row 4 =======================

Category = StringVar()  # Matt: allows Category to display a string
CCategory = ttk.Entry(F1, textvariable=Category, font=(None, 18))  # attributes for Category on GUI
CCategory.grid(row=4, column=1, padx=5, pady=5, sticky='w')  # Grid features for Category

# ===========tree view===========

TVList = ['Date', 'Title', 'Expense', 'Category']
TVExpense = ttk.Treeview(F1, column=TVList, show='headings', height=5)
for i in TVList:
    TVExpense.heading(i, text=i.title())
TVExpense.grid(row=4, column=1, padx=5, pady=5, sticky='w', columnspan=3)

GUI.mainloop()
