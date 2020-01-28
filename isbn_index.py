# Program name: ISBN
# Writen by: Firus Hanov
# Date: 01/18/2018

# ====================================
# Good
def createIndex():
    myDict = { }
    return myDict

# ====================================
# Good
def recordBook (index, ISBN, title ):
    index[ISBN] = title
# ====================================
# Good
def findBook(index, ISBN):
    for num in index:
        if num == ISBN:
            return index[ISBN]
        else:
            return ""
# ====================================
# Good

def listBooks(index):
    myList = []
    my_number = 1
    for ISBN in index:
        title = index[ISBN]
        myList.append(str(my_number)+" " + ISBN + " "+ title,)
        my_number += 1
    return myList

# ====================================
# Good
def formatMenu():
    a = 'What would you like to do?'
    b = '[r] Record a Book'
    c = '[f] Find a Book'
    d = '[l] List all Books'
    e = '[q] Quit'
    myList = [a,b,c,d,e]
    # return myList

    # new_list = [ ]
    for i in range(len(myList)):
        print(myList[i])



# ====================================
# Good
def formatMenuPrompt ():
    a = 'Enter an option: '
    return a


# ====================================
# Good
def getUserChoice(prompt):
    a = input(prompt)
    a = a.strip()
    while a == '':
        a = input(prompt)
        a = a.strip()
    return a

# ====================================
# Good
def getISBN ():
    ISBN = getUserChoice("Enter an ISBN: ")
    return ISBN

# ====================================
# Good
def getTitle ():
    title = getUserChoice("Enter a book title: ")
    return title


# ====================================
# Good
def recordBookAction (index ):
    ISBN = getUserChoice("Enter an ISBN: ")
    title = getUserChoice("Enter a book Title: ")
    index[ISBN] = title

# ====================================
# OK
def findBookAction ( index ):
    ISBN = getISBN()
    f = findBook(index, ISBN)
    if f:
        print(index[ISBN])
    else:
        print("The book doesn't exist in our database. ")

# ====================================
# Good

def listBooksAction (index):
    ans = listBooks(index)
    if ans == []:
        print("No book found! ")
    else:
        for num in ans:
            print(num + "\n")



# ====================================
# Good

import sys
def quitAction (index):
    print("The program is ending...")
    sys.exit ( 0 )

# ====================================
# Good


def applyAction(index, choice):
    if choice == "r":
        recordBookAction(index)
    elif choice == "f":
        findBookAction(index)
    elif choice == "l":
        listBooksAction(index)
    elif choice == "q":
        quitAction(index)
    else:
        print("The following command doesn't exist")

# ====================================

def main ():
    my_index = createIndex()

    while True:
        format_menu = formatMenu()
        user_input = getUserChoice("Enter your choice: ")
        applyAction(my_index, user_input)



# ====================================
if __name__ == '__main__':
    main( )








