import mysql.connector

class DbHelper:

    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="library")
            self.mycursor = self.conn.cursor()
        except:
            print("Could not connect to database")
            exit()



    def fetch_data(self):
        self.mycursor.execute("SELECT * FROM `library`")
        data = self.mycursor.fetchall()

        return data



    def update_info(self, book_name_input, book_catagory_input, book_number_input):


        try:
            self.mycursor.execute("""
                                                                        INSERT INTO library (Name,Catagory,Numbers)
                                                                        VALUES
                                                                        ('{}','{}',{})
                    """.format(book_name_input, book_catagory_input, book_number_input))

            self.conn.commit()
            return 1
        except:
            return 0



    def issueBook(self, book_name_input, book_id_input):

        try:
            self.mycursor.execute('SELECT * FROM `library` WHERE Name LIKE "{}"'.format(book_name_input))
            data = self.mycursor.fetchall()



            number = data[0][3] - 1



            self.mycursor.execute("UPDATE `library` SET `Numbers` = {} WHERE `library`.`SNo.` = {}; ".format(number, book_id_input))
            self.conn.commit()

            return 1


        except:

            return 0


    def bookReturn(self, book_name_input):

        try:
            self.mycursor.execute('SELECT * FROM `library` WHERE `library`.`Name` = "{}"'.format(book_name_input))
            data = self.mycursor.fetchall()

            number = data[0][3] + 1



            self.mycursor.execute(
            "UPDATE `library` SET `Numbers` = {} WHERE `library`.`Name` = '{}' ".format(number, book_name_input))
            self.conn.commit()

            return 1

        except:

            return 2




# SELECT * FROM `library` WHERE `library`.`Name` = "Let Us C"

# sayan = DbHelper
#
# sayan.fetch_data()
#
# UPDATE
# `library`
# SET
# `Numbers` = '2'
# WHERE
# `library`.
# `SNo.` = 2;


# UPDATE `library` SET `Numbers` = '3' WHERE `library`.`Name` = "Let Us C"