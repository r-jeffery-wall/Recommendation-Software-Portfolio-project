from locations import locations
from alphabetise import alphabetise

# Initial variable declarations. This should allow the program to be more dynamic.
city = "Istanbul"
categories = [category for category in locations[list(locations.keys())[0]]]

# The welcome message will greet the user, perform initial set up, and pass on to other functions to complete a run of the program.
def welcome():
    print(f"Welcome to the City guide for {city}. You can search here for recommendations based on a number of categories: ")
    print("After searching, a filtered list will be displayed that you can then search again to filter your results further.")
    print("We hope you enjoy your time using this software.")
    print("First things first, let's choose a category to search. The available categories are: ")
    print_data(categories)
    category = choose_category(categories)
    category_alphabetised = alphabetise(category, locations)
    see_options = input("Would you like to see a list of all available options in this category? Y/N")
    if yes_no(see_options):
        show_options(category_alphabetised)
    search_term = input("Please enter a search term to choose a category. Enter a character to see all options beginning with that letter or enter a term to find matching results: ")
    search_key = autocomplete(search_term, category_alphabetised)
    search(search_key, category)

# This function is used to autocomplete search results and return the search term the user wants to use.
def autocomplete(search, category):
    # The autocomplete executed will vary depending on whether one character is inputted or not.
    if len(search) == 1:
        search_results = category.retrieve(search.upper())
    else:
        search_results = []
        for lst in category.array:
            for item in lst:
                if search in item.lower():
                  search_results.append(item)
    if len(search_results) == 0:
        print("No matches found!")
        autocomplete(search, category)
    else:
        print_data(search_results)
    if len(search_results) > 1:
        choice_index = int(input("Please choose a search term from the list of results by entering it's number: "))
        while choice_index > len(search_results) or choice_index <= 0:
            choice_index = int(input("Invalid choice. Please select a number matching one of the options above: "))
        choice = search_results[choice_index - 1]
    else:
        choice = search_results[0]
    print(f"You have chosen: {choice}")
    choice_correct = input("Is this correct? Y/N: ")
    if yes_no(choice_correct):
        return choice
    else:
        autocomplete(search, category)

# Helper function for printing results in a cleaner way.
def print_data(results):
    for item in results:
        print(f"- {item}.")

# Helper function for handling yes/no input.
def yes_no(input):
    # This handles the case when the user just presses enter, which will be taken as yes.
    if input == None:
        return True
    elif input[0].lower() == 'y':
        return True
    else:
        return False

# Prints a list of all the options available to the user in a certain category. When refactoring - add a sort to make this list alphabetic.
def show_options(alphabetised_dict):
    for lst in alphabetised_dict.array:
        for item in lst:
            if len(item) > 0:
                print(f"-{item}")

# As the search term is already chosen by this point, the search just needs to return a list of locations that have a matching value in the chosen category.
def search(search_term, category):
    results = []
    for location in list(locations.keys()):
        # The code needs to behave differently if the category contains more than one item.
        if type(locations[location][category]) == tuple:
            if search_term in locations[location][category]:
                results.append(location)
        else:
            if locations[location][category] == search_term:
                results.append(location)
    if len(results) == 0:
        print("No results found!")
    else:
        print("Results: \n")
        for item in results:
            print(f"- {item}\n")

# This helper function creates a dictionary that contains an alphabetised dictionary for each category. This will help with autocompletion and the retrieval of results.
def create_alphabetised_categories(categories):
    alphabetised_categories = {}
    for category in categories:
        alphabetised_categories[category] = alphabetise(category, locations)
    return alphabetised_categories

# Helper function to list the choices that are available to the user in a certain category.
def print_data(data_type):
    for i in range(0, len(data_type)):
        print(f"{i + 1}: {data_type[i]}") 

def choose_category(category_list):
    choice = input("Please choose a category by inputting the number associated with it: ")
    if choice.isalpha() or int(choice) > len(category_list) or int(choice) <= 0:
        print(f"Invalid choice. Please enter a number between 1 and {len(category_list)}.")
        choose_category(category_list)
    else:
        print("You have chosen: " + category_list[int(choice) - 1])
        choice_correct = input("Is this correct? Y/N: ")
        if yes_no(choice_correct):
            return category_list[int(choice) - 1]
        else:
            choose_category(category_list)

welcome()
