# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MHamilton,12.5.2021,Initial modification of code to complete assignment 8
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

    # Class attribute to track total number of products.
    totalProd = 0

    @staticmethod
    def status():
            print("The total number of products is: ", totalProd)

    # Constructor method
    def __init__(self, name, price):
        """A product and a price"""
        self.name = name
        self.price = price
        print("A new product has been added. Name: ", self.name, ", Price: ", self.price)
        Product.totalProd += 1



# Data -------------------------------------------------------------------- #



# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

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
    pass
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #



# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

prod_name = input("Please enter product name: ")
prod_price = input("Please enter product price: ")

p1 = Product(prod_name, prod_price)
print(Product.totalProd)



# Main Body of Script  ---------------------------------------------------- #

