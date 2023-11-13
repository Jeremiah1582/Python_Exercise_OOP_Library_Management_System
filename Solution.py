import random 
from classes import Patron, Library, Book

if __name__ == "__main__":
    
    def testCase():
        book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769174")
        book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
        book3 = Book("1984", "George Orwell", "9780451524935")
        patron1 = Patron("Alice",'alice@alice.com', "12345")
        patron2 = Patron("Bob",'bob@bob.com', "54321")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.register_patron(patron1)
        library.register_patron(patron2)
        library.borrow_book(patron1, book1)
        print(patron1, book1)
        library.borrow_book(patron2, book2)
        library.return_book(patron1, book1)
    library = Library()
    testCase()
    
    
    while True:
        # list patrons names
        patronName=[*map(lambda x:x.name, library.patrons)] #list of patron names
        print(patronName)
        
        
        # creating a login state
        login ={ 
                'userName': input('userName: '),
                'emailAddress': input('Email address: '),
                'cardNum': input('Card Number: ')
                }
        
        print('userName.......', login['userName'])
        if login["userName"] in patronName : 
            print(f'\nHello {login["userName"]} you are logged in !\n')
            break 
        else:
            print('\nUser does not exist: Please Register')
            choice=input('\nwould you like to register now? Y/N: ')
            print('---------------------')
            if choice.lower() != 'y':
                print('\nOk, check your details and try again!>>>')
                continue
            else:            
                newPatron = Patron(
                    name=input('enter your Name: '),
                    email=input('enter Email address: '),
                    card_number=random.randint(10000,99999)
                )
                library.register_patron(newPatron)
                print(f'New Patron {newPatron.name} added, ref:{newPatron.card_number}') 
                print(f"\n Welcome {newPatron.name}, you've successfully registered, \n  and we have logged you in \n")
                break
        
    while True: 
        print('1) list Books')
        print('2) list Patrons')
        print('3) list Transactions')
        print('4) add book')
        print('5) borrow Book ')
        print('6) logout ')
               
        choice= int(input('select a number: '))
        # instances
        
        match choice: #switch statement 
            
            case 1:#List books
                library.display_books()
                print('------------------\n')
            case 2: #list Patrons
                library.display_patrons()
                print('------------------\n')
            case 3: #display transaction
                library.display_transactions()
                print('------------------\n')
            case 4: #add books
                newBook = Book(
                    title=input('what is the books title?: ' ),
                    author=input('Who is the author?: '),
                    refNum= random.randint(100000000,999999999)#generate random num between a-b
                    )
                library.add_book(newBook)
                print(f'\nnew book added: \n{newBook.title}\n{newBook.author}\n{newBook.refNum}')
                print('------------------\n')
            case 5: #Borrow Book
                print('you are....',login['userName'])
                
                library.borrow_book(login=Patron(), book= Book())
            case _: 
                print('Option not Valid')






