#
# Model a library book using a class with instance attributes and a method

# Create a class Book with instance attributes title, author, and is_borrowed (default False, set manually after creation). Add a method display_info() that prints all three attributes in a readable sentence. Create 3 different Book objects and call display_info() on each, confirming each object holds independent data.


class Book :
    def __init__(self,title,author,is_borrowed =False):
        self.title=title
        self.author=author 
        self.is_borrowed =is_borrowed


    def display_info(self):
        print(f"Hello ! dear user...\nTitle of the Book is : {self.title}\nThe Author of the Book is : {self.author}\nBook is Borrowed : {self.is_borrowed}")
        print("\n")


book1=Book("Ramayan","Valmiki")
book1.display_info()

book2 = Book("Mahabharat", "Ved Vyasa","True")      # set manually True
book2.display_info()

book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam","True")      # set manually True
book3.display_info()


