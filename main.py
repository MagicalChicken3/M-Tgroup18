'''
NetID's: dz183
Purpose: This is the main file containing all the classes and calls to the database. This is a imitation of a book store that users can buy books from. 
'''

#import pymysql

# Will add sql calls into the init to add to database
class User:
    def __init__init(self, name, username, password, address, city, state, zip, paymentinfo, shippinginfo):
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.paymentinfo = paymentinfo
        self.shippinginfo = shippinginfo
    
    def RegisterUser(self):
        self.name = input("What is your name?")
        self.username = input("What is your username?")
        self.password = input("What is your password?")
        self.address = input("What is your address?")
        self.city = input("What is your city?")
        self.state = input("What is your state?")
        self.zip = input("What is your zip code?")
        self.paymentinfo = input("What is your payment type? Card or Cash")
        self.shippinginfo = input("What is your shipping address?")
        print("Account created: " + self.username)
        # Call SQL queries here
        
        
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
		
class Inventory(Books):
    def __init__(self, title, author, genre, isbn, stock, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.stock = stock
        self.price = price
	    # Call a sql query to the book database and add a book
	
    #def search_Book():
    ## This would do a sql query where it would search the inventory database and using the isbn, search the book database
    #def viewInventory():
    #def increaseStock():
    #def decreaseStock():
	    
class Cart():
    def __init__(self, username, cartNumber, title, isbn, number, price, total):    
        self.username = username
        self.cartNumber = cartNumber
        self.title = title
        self.isbn = isbn
        self.number = number
        self.price = price
        self.total = total
        
def main():
    
    # This menu table is for the menu system to print out the message/options
    menu = {}
    menu['1']="View User Info." 
    menu['2']="Cart Information"
    menu['3']="Checkout Cart"
    menu['4']="View Store Items"
    menu['5']="Log out"

    while True:   
        print ("Welcome to the store!")
        print (" 1: Login")
        print (" 2: Register User")
        print (" 3: Exit")
        pre_login = int(input("How can we help you?"))
       
        if pre_login == 1: 
           # This is the login menu
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
                  
                # This exits the menu; not the program
                elif choice == 5:
                    print ("You have been logged out.")
                    break
                else: 
                  print ("Invalid Menu option. Please try again!")
        
        # This will create a new user just by calling the class
        elif pre_login == 2:
            New_user = User()
            New_user.RegisterUser()
        
        # Will exit the program
        elif pre_login == 3:
            print ("Have a nice day!")
            break
main()
