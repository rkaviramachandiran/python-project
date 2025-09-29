# Python Version 3.13.6
# To import python Package is json and csv used to store Book list in File

import json
import csv

# Creat constructor class For to define title author rating 
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.rating=None
    
# Creat a function for rating a book 
        
    def set_rating(self,rating):
        self.rating=rating
        
# creating a class for book clup operation 
   
class book_club():
    def __init__(self):
       self.list=[ ] #creat emty list
       
# Add book to the book clup to using append keyword take title and author from constructor class
      
    def add(self,title,author):
        book=Book(title,author)
        self.list.append(book)
        print(f"Book {title} Successfully Added To the Book Clup...")
        print("\n")
    
# Remove book first title passed to the remove operation function and 
# check title.lower equal to title.lower then true remove the book using remove keyword      
    
    def  remove_book(self,title):
        for book in self.list:
            if book.title.lower()==title.lower():
                self.list.remove(book)
                print(f"Book {title} Successfully Removed To the Book Clup...")
                print("\n")
                return
        print(f"Book {title} Not Found To the Book Clup")
        print("\n")
        
#rating to the book , get input passing the title and rating check title.lower equal to title.lower then true 
# call set rating function and store rating
   
    def rate_book(self,title,rating):
        for book in self.list:
            if book.title.lower()==title.lower():
                book.set_rating(rating)
                print(f"Book {title} Star {rating}.")
                print("\n") 
                return
        print(f"Book {title} Not Found To the Book Clup")
        print("\n")
     
# Display the book list first call display book function and print title , author and rating
        
    def display_book(self):
        for book in self.list:
             print(f"Title {book.title} Author {book.author} Rateing(1-5) {book.rating}") 
             print("\n")
             
    def export_to_json(self,filename):# passing filename to export to json
        data=[] #creat emty list 
        for book in self.list: # using for loop to apppend title author and rating to store data variable list
            data.append({
                "Title":book.title,
                "Author":book.author,
                "Rating":book.rating
            }) 
            with open(filename,"a",newline="") as f: # using with keyword and open function to set filename append mode('a') and newline as f name
                json.dump(data,f)
            print(f"Book export to {filename} file")
            print("\n")
            
    def export_to_csv(self,filename):
        with open(filename,'a',newline="") as c:
            writer=csv.writer(c)
            writer.writerow(["Title","Author","Rating"])
            for book in self.list:
                writer.writerow([book.title,book.author,book.rating])
        print(f"Book export to {filename} file")
        print("\n")    
                
Book_club=book_club() # create Book_club object for book_club class 
while True: # using for program cotinues running
    
    # create few book club operation like add book ,remove book ,display book ,export file exct.,   
          
      print( " BOOK CLUB MENU\n "
            " 1.Add Books to Book Clup\n"
            "  2.Remove a Book \n"
            "  3.Rate Book\n"
            "  4 Display All Books\n"
            "  5.Export to json\n"
            "  6.Expot to csv\n"
            "  7.Exit")
      
      operation=int(input("enter your operation:")) # get input from user 
      if operation == 1: 
          title=input("Enter Book Title:") # get input title and author 
          author=input("Enter Author Name:")  
          Book_club.add(title,author) # and pass the values to add function 
    
      elif operation == 2:
          title=input("Enter Book Title:") # get input title
          Book_club.remove_book(title) # and pass the value to remove function 
        
      elif  operation == 3:
          title=input("Enter title:")  # get input title
          rating=int(input("Enter rating(1-5):"))  # get input rating
          Book_club.rate_book(title,rating) # and pass the value to rating function 
          
      elif operation == 4:
          Book_club.display_book() #just call display function
          
      elif operation == 5:
          filename=input("Enter File name (e.g. books.json):") #
          Book_club.export_to_json(filename)
          
      elif operation == 6:
          filename=input("Enter File name (e.g. books.csv):")
          Book_club.export_to_csv(filename)
        
      elif operation == 7:
          print("Good Bey...!")
          break
      else :
          print("Invaild option , Please Try againe....")