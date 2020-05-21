from tkinter import *
from tkinter import messagebox

from dbhelper import DbHelper


class Library:

    def __init__(self):

        self.db = DbHelper()

        self.mainWindow()



    def mainWindow(self):
        self.root = Tk()

        self.root.maxsize(400, 600)
        self.root.minsize(400, 600)
        self.root.config(background="#12F1DA")

        self.root.title("Library")



        self.label = Label(text="Welcome to the Library", bg="#12F1DA")
        self.label.config(font=(30))
        self.label.pack(pady="20 10")

        self.show_book_button = Button(self.root, text="See available Book", bg="#09A898", width=25, height=2,
                                       command=lambda: self.see_book())
        self.show_book_button.pack(pady=(40, 10))

        self.add_book_button = Button(self.root, text="Add Book", bg="#09A898", width=25, height=2, command=lambda: self.add_book())
        self.add_book_button.pack(pady=(40, 10))

        self.fetch_book_button = Button(self.root, text="Issue Book", bg="#09A898", width=25, height=2, command=lambda: self.book_issue())
        self.fetch_book_button.pack(pady=(40, 10))

        self.return_book_button = Button(self.root, text="Return Book", bg="#09A898", width=25, height=2, command=lambda: self.book_return())
        self.return_book_button.pack(pady=(40, 10))

        self.headerMenu()

        self.root.mainloop()




    def book_return(self):

        self.clear()

        self.book_name_label = Label(self.root, text="Book Name:", fg="#fff", bg="#09A898")
        self.book_name_label.config(font=("Arial", 16))
        self.book_name_label.pack(pady=(20, 10))

        self.book_name_input = Entry(self.root)
        self.book_name_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        self.book_catagory = Label(self.root, text="Book Category:", fg="#fff", bg="#09A898")
        self.book_catagory.config(font=("Arial", 16))
        self.book_catagory.pack(pady=(20, 10))

        self.book_catagory_input = Entry(self.root)
        self.book_catagory_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        book_return_button = Button(self.root, text="Return", width=25, height=2, bg="#09A898", command = lambda: self.bookReturn())

        book_return_button.pack(pady=(10, 10))




    def bookReturn(self):

        flag = self.db.bookReturn(self.book_name_input.get())

        if flag ==1:
            messagebox.showinfo("Success", "You returned the book")

        else:
            messagebox.showerror("Error", "Error!! You entered the wrong book name or there is some technical issue")




    def book_issue(self):

        self.clear()

        book_issue_button = Button(self.root, text="Show available books", width=25, height=2, bg="#09A898", command=lambda: self.see_book())
        book_issue_button.pack(pady=(10,10))

        self.book_id = Label(self.root, text="Book Id:", fg="#fff", bg="#09A898")
        self.book_id.config(font=("Arial", 16))
        self.book_id.pack(pady=(20, 10))

        self.book_id_input = Entry(self.root)
        self.book_id_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        self.book_name_label = Label(self.root, text="Book Name:", fg="#fff", bg="#09A898")
        self.book_name_label.config(font=("Arial", 16))
        self.book_name_label.pack(pady=(20, 10))

        self.book_name_input = Entry(self.root)
        self.book_name_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        self.issue_book = Button(self.root, text="Issue Book", bg="#09A898", width=25, height=2, command=lambda: self.issueBook())
        self.issue_book.pack()




    def issueBook(self):


        flag = self.db.issueBook(self.book_name_input.get(), self.book_id_input.get())


        if flag==1:
            messagebox.showinfo("Success", "You issued the book.")

        else:
            messagebox.showerror("Error", "Failed!!! Try again")





    def add_book(self):

        self.clear()

        self.book_name_label = Label(self.root, text="Book Name:", fg="#fff", bg="#09A898")
        self.book_name_label.config(font=("Arial", 16))
        self.book_name_label.pack(pady=(20, 10))

        self.book_name_input = Entry(self.root)
        self.book_name_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        self.book_catagory = Label(self.root, text="Book Category:", fg="#fff", bg="#09A898")
        self.book_catagory.config(font=("Arial", 16))
        self.book_catagory.pack(pady=(20, 10))

        self.book_catagory_input = Entry(self.root)
        self.book_catagory_input.pack(pady=(5, 80), ipady=10, ipadx=70)

        self.book_number = Label(self.root, text="No of book(s):", fg="#fff", bg="#09A898")
        self.book_number.config(font=("Arial", 16))
        self.book_number.pack(pady=(20, 10))

        self.book_number_input = Entry(self.root)
        self.book_number_input.pack(pady=(5, 50), ipady=10, ipadx=70)

        self.add_button = Button(self.root, text="Click to add",bg="#09A898", width=25, height=2, command=lambda: self.add_data())
        self.add_button.pack()




    def add_data(self):


        flag = self.db.update_info(self.book_name_input.get(), self.book_catagory_input.get(), self.book_number_input.get())

        if flag ==1:
            messagebox.showinfo("Successful", "Added the data successfully")

        else:
            messagebox.showerror("Error", "The data was not added successfully")



    def see_book(self):

        # Mera DB ka name library and table ka name bhi library. In library there are 4 columns --> SNo. , Name, Category, Numbers
        # Numbers mean how many books are present in it and SNo. is auto-increament

        self.clear()

        self.book_name = self.db.fetch_data()

        # scrollbar = Scrollbar(self.root)
        # scrollbar.pack(side=RIGHT, fill=Y)
        # mylist = Listbox(self.root, yscrollcommand = scrollbar.set )

        for i in self.book_name:

            if i[3] > 0:
                book_id = "Book id:   " + str(i[0])
                book = "Book:     " + i[1]
                book_count = "Avalable No of Books = " + str(i[3])

                book_id_label = Label(self.root, text=book_id,  bg="#A7EDE6")
                book_id_label.pack(pady=(10,20))

                book_label = Label(self.root, text=book,  bg="#A7EDE6")
                book_label.pack(pady=(2, 20))

                book_count_label = Label(self.root, text=book_count, bg="#A7EDE6")
                book_count_label.pack(pady=(2, 20))

                self.horizontal_line = Label(text="----------------------------------------------------------------", bg="#12F1DA")
                self.horizontal_line.pack()

        self.issue_button = Button(self.root, text="Click to issue book", width=25, height=2, bg="#09A898", command=lambda: self.book_issue())
        self.issue_button.pack(pady=(10,10))

        # mylist.pack(side=LEFT, fill=BOTH)
        # scrollbar.config(command=mylist.yview)

    def headerMenu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Menu", menu=filemenu)
        filemenu.add_command(label="Show", command=lambda: self.show_book())
        filemenu.add_command(label="Add", command=lambda: self.add_book())
        filemenu.add_command(label="Issue Book", command=lambda: self.book_issue())
        filemenu.add_command(label="Return", command=lambda: self.book_return())



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()








obj = Library()

