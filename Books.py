# NetId dz183
# This is the headerpy file containing the class Books
class Books
	def __init__(self, title, author, genre, isbn, price)
		self.title = title
		self.author = author
		self.genre = genre
		self.isbn = isbn
		self.price = price
	def updateprice(self, new_price)
		# This needs to be testedchange for the database. 
		self.price = new_price
		


Everything below is to test the class
	
book1 = Books(Harry Potter and the Sorceror Stone, J.K. Rowling, Fantasy, 9780590353403, 6.98)
print(book1.title)
print(book1.author)
print(book1.genre)
print(book1.isbn)
print(book1.price)

book1.updateprice(5.99)
print(book1.price)

