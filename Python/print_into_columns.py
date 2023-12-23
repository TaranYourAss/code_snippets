def print_into_coulmns(list_:list, num_columns:int=2, colour:str=""):
    """
    Prints a list into the provided number of columns.
    """
    if type(list_) is not list:
        raise Exception(f"Argument 'list' must be a list data type. - {type(list_)}")
    
    if type(num_columns) is not int:
        raise Exception("Argument 'num_columns' must be an integer data type.")

    # Calculate the number of rows needed
    num_rows = -(-len(list_) // num_columns)

    # Iterate through the rows and print the list items into columns
    for row in range(num_rows):
        for col in range(num_columns):
            index = row + col * num_rows
            if index < len(list_):
                print(f"{colour}{list_[index]:<20}", end="")
        print()  # Move to the next line for the next row
