class Book:
    def __init__(self,title,author,NumPages):
        self.title = title
        self.author = author
        self.NumPages = NumPages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.NumPages == other.NumPages
    
    def __lt__(self, other):
        return self.NumPages < other.NumPages
    
    def __gt__(self, other):
        return self.NumPages > other.NumPages
    
    def __add__(self,other):
        return self.NumPages + other.NumPages
    
    def __contains__(self, keyword):
        return keyword in self.title or self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        if key == 'author':
            return self.author
        if key == "NumPages":
            return self.NumPages
        else:
            return f"Key {key} was not found"
book1 = Book("The Hobit","J.R.R",310)
book2 = Book("Harry Potter","J.K.R",223)
book3 = Book("The Lion","C.S.L",172)
book4 = Book("The Hobit","J.R.R",310)

print(book1)
print(book1==book2)
print(book1==book4)
print(book2>book3)
print(book2+book3) 
print("Lion" in book3)
print(book1['title'])
print(book1['author'])
print(book1['NumPages'])