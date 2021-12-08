# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MHamilton,12.5.2021,Initial modification of code to complete assignment 8
# MHamilton,12.7.2021,Updated code and improved commenting
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
        output_total_number_of_products: (static) prints total number of products

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MHamilton,12.5.2021,Modified code to complete assignment 8
    """

    # -- Class attribute to track total number of products --
    totalProd = 0

    # -- Static method to get number of products --
    @staticmethod
    def output_total_number_of_products():
        print("The total number of products is: ", Product.totalProd)

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
        read_data_from_file(file_name): -> (a list of product objects)
        write_data_to_file(file_name, prod_list):

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
                line = line.strip()
                if not line:
                    continue
                in_name, in_price = line.split(",")
                # create object with these values
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
        :param prod_list: (list) you want filled with file data:
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

        methods:
            show_menu_tasks: shows menu of options to user
            input_menu_choice: get choice from user
            show_current_products_in_list: display all products currently held
            input_new_product: allow user to add new product and price

        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            MHamilton,12.5.2021,Modified code to complete assignment 8
            MHamilton,12.7.2021,Updated code and comments
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
            return(choice)
        except:
            raise Exception("Please enter a numeric value between 1 and 4.")
            print()  # Add an extra line for looks

    # -- Method to show the current data from the file to user --
    @staticmethod
    def show_current_products_in_list(prod_list):
        """ Shows the current Tasks in the list of objects

        :param prod_list: (list) of objects you want to display
        :return: nothing
        """
        Product.output_total_number_of_products()
        print()  # Add an extra line for looks
        print("******* The current products are: *******")
        for obj in prod_list:
            print(obj.product_name + "," + obj.product_price)
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

# Display a menu of choices to the user
while (True):
    IO.show_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':  # Show current list
        # Show current data in the list/table
        IO.show_current_products_in_list(lstOfProductObjects)
        continue  # to show menu

    elif choice_str.strip() == '2':  # Add a new Task
        # First get new input from user (a task and a priority)
        new_obj = IO.input_new_product()
        # Now add that data to the list
        lstOfProductObjects.append(new_obj)
        # Remove object
        del new_obj
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        # Here we write to file using pre-defined filename
        FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #

