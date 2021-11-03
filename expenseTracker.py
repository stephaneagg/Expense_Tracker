import csv
import Purchase as p
import Date as d
purchases = []


# (none -> none)
# function is used to verify user
# takes input and checks if it is a valid username
def login():
    login = False
    while (login == False):
        username = input("\nUsername - ")
        if (username == "user"):
            login = True
            print("\nWelcome\n")
        elif (username == "quit"):
            return
        else:
            print("incorrect login \n")
    update_purchases()
    interface()

# (none ->)
# function is used to determine what function should be called
# based on user input
def interface():
    done = False
    while (done == False):
        user = input("\nWhat would you like to do? \nValid inputs are: add expense, list expenses, help, quit \n- ")
        if user == "add expense":
            add()
            continue
        if user == "list expenses":
            user = input("Would you like to see a table of all expenses? (yes/no) - ")
            if user == "yes":
                toString()
                continue
            if user == "no":
                print(expense())
                continue
        if user == "help":
            help()
            continue
        if user == "quit":
            return
        else:
            print("Invalid input")


# (none -> none)
# function adds an entry to the csv
# entry is formated as DATE,
# DATE is formated as MM DD YYYY
# AMOUNT is formated as a float
def add():
    done = False
    while (done == False):
        date = input("\nfor help with formating enter help -> dateFormat \nplease enter date (MM DD YYYY) - ")
        if date == "quit":
            return
        ##
        ##checking to make sure date is valid
        los = date.split(" ")
        try:
            test = d.Date(los[0], los[1], los[2])
        except IndexError:
            print("Invalid date")
            return
        if (test.isValid() == False):
            print("Invalid date")
            return
        ##
        while (done == False):
            correct = input("you've entered \'" + date + "\' is this correct? \nenter \'yes\' or \'no\' - ")
            if (correct == "yes"):
                done = True
            else:
                break


    done = False
    while (done == False):
        price = input("\nfor help with formating enter help -> amountFormat \nplease enter amount spent - ")
        ##
        ## testing if price is a valid number
        try:
            float(price)
        except ValueError:
            print("invalid price")
            return
        if price == "quit":
            return
        if price == "help":
            help()
        while (done == False):
            correct = input("you've entered \'" + price + "\' is this correct? \nenter \'yes\' or \'no\' - ")
            if (correct == "yes"):
                done = True
            else:
                break

    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, price])

    print("\nentry added to list\n")
    update_purchases()

# (none -> none)
# function prints instuctions to use the program
# based on user input
def help():
    print("\nWhich functions would you like help with: add expense, list expenses")
    user = input("-")
    if user == "add expense":
        print("\nadd expense is used to add an expense")
        print("Would you like help with Date Format or Amount Format?")
        user1 = input("-")
        if user1 == "Date Format" or "date format":
            print("\ndate must be formated as MM DD YY seperated by spaces ex. 01 01 2020")
        if user1 == "Amount Format":
            print("\namount must be formated as a number. Decimals are supported ex. 100.00")
    if user == "list expenses":
        print("\nlist expenses is used to view your expenses")
        print("You can view a table of all expenses, view your total expense or view your total expense up to a specified date")
    else:
        print("invalid input")
# (none -> none)
# function updates the list with values in the csv
# this function is called on login and whenever the csv is changed
# if the user input is invalid function calls methods to repair
# purchases and the csv
def update_purchases():
    global purchases
    newList = []
    file_handle = open('expenses.csv', 'r')
    for line in file_handle:
        line = line.strip()
        los = line.split(",")
        if (len(los) == 2):
            try:
                lod = los[0].split(" ")
                date = d.Date(lod[0], lod[1], lod[2])
                amount = float(los[1])
                purchase = p.Purchase(date, amount)
                newList.append(purchase)
            except ValueError:
                print("\ninvalid type format in csv\n")
    purchases = newList


# (none -> String)
# function returns a table in the form of a string
# representing all elements in the csv
def toString():
    global purchases
    print("\n-----------------------------------")
    print("Date \t\t |\tAmount\t  |")
    print("-----------------------------------")
    for i in purchases:
        print('%-17s%-17s' % (i.get_date().toString(), " $" +str(i.get_price())))
    print("-----------------------------------\n")

# (none -> none)
# function removes the last element from list of purchases
# should also remove the last element from the csv file but doesnt do that yet
def remove_last():
    global purchases
    index = len(purchases)-1
    purchases.pop(index)
    # file_handle = open('expenses.csv', 'r')
    # n = 0
    # for line in file_handle:
    #     if n == index:
    #
    #     n+=1

# (none -> none)
#
def expense():
    global purchases
    user = input("\nIf you would like to see your total expense enter \"all\"\nIf you would like to see your total expenses up to a certain date enter \"limited\" - ")
    if user == "all":
        total = 0
        for purchase in purchases:
            total += purchase.get_price()
        return str("$"+str(total) + " is your total expense\n")
    if user == "limited":
        return(limitedExpense())

def limitedExpense():
    total = 0
    user = input("Until what date would you like to see your expenses? (MM DD YYYY) - ")
    los = user.split(" ")
    try:
        date = d.Date(los[0], los[1], los[2])
        if (date.isValid() == False):
            return("invalid date")
    except IndexError:
        return("invalid date")
    for purchase in purchases:
        if purchase.get_date().isBefore(date):
            total+=purchase.get_price()
    return str("Your total expenses up until " + date.toString() + " is " + "$" + str(total) + "\n")


def main():
    login()

main()
