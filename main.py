'''
NetID's: dz183
Purpose: This is the main file containing all the classes and calls to the database. This is a imitation of a book store that users can buy books from. 
'''

class Books:
	def __init__(self, title, author, genre, isbn, price):
		self.title = title
		self.author = author
		self.genre = genre
		self.isbn = isbn
		self.price = price
	def updateprice(self, new_price):
		# This needs to be testedchange for the database. 
		self.price = new_price

def main():
    
    # This menu table is for the menu system to print out the message/options
    menu = {}
    menu['1']="View User Info." 
    menu['2']="Cart Information"
    menu['3']="Checkout Cart"
    menu['4']="View Store Items"
    menu['5']="Log out"
   
   #This is the login menu
    while True:
        print ("Enter Username and Password")
        username = input ("Username: ")
        password = input ("Password: ")
        #part after this will have to check the database and call break if it is in the database to exit this while loop
        break
       
    # This is the store menu    
    while True: 
        for key in menu.keys():
            print (key, '--', menu[key] )

        # User will decide/input option
        choice=int(input("Please Select:")) 
        
        # Once User has inputted their choice, check for path
        if choice == 1: 
            print ("View User Info")
        elif choice == 2: 
          print ("Cart Information")
        elif choice == 3:
          print ("Checkout Cart")
        elif choice == 4: 
          print ("View Store Items")
        elif choice == 5:
            print ("You have been logged out. Have a nice day!")
            break
        else: 
          print ("Invalid Menu option. Please try again!")
          
main()
