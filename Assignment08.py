# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MHamilton,12.5.2021,Initial modification of code to complete assignment 8
# MHamilton,12.7.2021,Updated code
# ------------------------------------------------------------------------ #


# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MHamilton,12.5.2021,Modified code to complete assignment 8
    """

    # -- Class attribute to track total number of products --
    totalProd = 0

    # -- Static method to get number of products --
    @staticmethod
    def status():
            print("The total number of products is: ", totalProd)

    # -- Constructor --
    def __init__(self, product_name, product_price):
        """A product and a price"""
        self.__product_name = product_name
        self.__product_price = product_price
        print("A new product has been added.")
        Product.totalProd += 1

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if value == "":
            print("A product must have a name.")
        else:
            self.__product_name = value
            print("Product has been renamed.")

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if value == "":
            print("A product must have a price.")
        else:
            self.__product_price = value
            print("Product has been re-priced.")

# Data -------------------------------------------------------------------- #



# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, prod_list):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MHamilton,12.7.2021,Modified code to complete assignment 8
    """

    # -- Method to process data from a file --
    @staticmethod
    def read_data_from_file(file_name, prod_list):
        """ Reads data from a file into a list of objects

        :param file_name: (string) with name of file:
        :param prod_list: (list) you want filled with file data:
        :return: (list) of objects
        """

        prod_list.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                in_name, in_price = line.split(",")
                # Here we make sure to convert all text to lower case to match with later
                # functionality.
                obj = Product(in_name, in_price)
                prod_list.append(obj)
            file.close()
            return prod_list
        except:
            print("File not found!")

    # -- Method to process data to a file --
    @staticmethod
    def write_data_to_file(file_name, prod_list):
        """ Write list of user-defined product names/prices to file

        :param file_name: (string) user-defined filename for output:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: nothing
        """
        # Process the data into a file
        outfile = open(file_name, "w")
        for obj in prod_list:
            outfile.write(obj.product_name + "," + obj.product_price + "\n")
        outfile.close()
        # Display a message to the user
        print("Data saved to file!")
        # Print extra line for space
        print()

# Processing  ------------------------------------------------------------- #



# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Presents information about the products:

        properties:
            xxx: (string) xxx

        methods:

        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            MHamilton,12.5.2021,Modified code to complete assignment 8
        """

    # -- Method to show menu to user --
    @staticmethod
    def show_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show current products
            2) Add a new product
            3) Save data to file      
            4) Exit program
            ''')
        print()  # Add an extra line for looks

    # -- Method to get user's choice --
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        try:
            choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
            print()  # Add an extra line for looks
            return choice
        except:
            print("Please enter a numeric value between 1 and 4.")
            print()  # Add an extra line for looks

    # -- Method to show the current data from the file to user --
    @staticmethod
    def show_current_products_in_list(prod_list):
        """ Shows the current Tasks in the list of objects

        :param list_of_rows: (list) of objects you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for obj in prod_list:
            print(obj.name + " (" + obj.price + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # -- Method to get product data from user --
    @staticmethod
    def input_new_product():
        """ Prompts user for new product (name and price) to add to list

        :return: name and price as an object:
        """
        print("Please enter a product and price: ")
        in_name = input("Enter a product name: ").strip().lower()
        in_price = input("Enter a price: ").strip().lower()
        # create object
        obj = Product(in_name, in_price)
        # return object
        return (obj)


# Presentation (Input/Output)  -------------------------------------------- #



# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

# Show user a menu of options
IO.show_menu_tasks()

# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

in_name = input("Please enter product name: ")
in_price = input("Please enter product price: ")
p1 = Product(in_name, in_price)
print(p1.product_name)
print(p1.product_price)
p1.product_name = 'BLARG'
p1.product_price = 6.99
print(p1.product_name)
print(p1.product_price)


# p1 = Product(prod_name, prod_price)
# lstOfProductObjects.append(p1)
#
# prod_name = input("Please enter product name: ")
# prod_price = input("Please enter product price: ")
# p2 = Product(prod_name, prod_price)
# print(Product.totalProd)
# lstOfProductObjects.append(p2)

print(len(lstOfProductObjects))


# Main Body of Script  ---------------------------------------------------- #

