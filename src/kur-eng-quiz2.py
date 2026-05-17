# ---------LIBRARY IMPORTS--------
import os
import random
import sys

# -------TODO:------
# finish all US states (add constant and function)
# finish all US cities (add constant and function)
# add guessing food name from specific state/city

# add correcting mistake functions

# make fillintheblanks accept game argument, then use it like {type} in var names <---------


# ------DONE-------
# * finish all US regions (change constant)
# * make functions take arguments, then proceed. for example: def choice_menu(type), if type = "US" then (us ifs)
# * add appending int to list (avoid repetitions)
# * actually use percentage calculation

# ---------VARIABLE DEFINITIONS--------
#
# for a country - requires: country_MAX_regions, country_MAX_states, country_regions_questions, country_regions_answers_lowercase, country_regions_answers_uppercase, country_regions_facts

# //////US variables

us_MAX_regions = 24
us_MAX_states = 11

# US regions
us_regions = ["NE", "SE", "NE", "SW"]
us_regions_questions = [
    "Venison steak: ",
    "Buffalo Meat Jerky: ",
    "Beef sandwich (no condiments or sauce): ",
    "Rocky Mountain Oysters: ",
    "Cincinnati Chilli: ",
    "Lobster: ",
    "Clam chowder: ",
    "Lutefisk: ",
    "Cherry pies: ",
    "Maple syrup: ",
    "Deep-dish pizza: ",
    "Hot dogs: ",
    "Cornmeal pancakes: ",
    "Popcorn and corn chips: ",
    "Runza: ",
    "Fruit salads and smoothies: ",
    "Pork tenderloin: ",
    "Boiled peanuts: ",
    "Scrapple: ",
    "Crab cakes: ",
    "Spicy pork ribs: ",
    "Schrimp and grits: ",
    "Fried chicken: ",
    "Burnt ends: ",
]
us_regions_answers_uppercase = [
    "NW",
    "NW",
    "NW",
    "NW",
    "NW",
    "NE",
    "NE",
    "NE",
    "NE",
    "NE",
    "NE",
    "NE",
    "SW",
    "SW",
    "SW",
    "SW",
    "SW",
    "SE",
    "SE",
    "SE",
    "SE",
    "SE",
    "SE",
    "SE",
]
us_regions_answers_lowercase = [
    "nw",
    "nw",
    "nw",
    "nw",
    "nw",
    "ne",
    "ne",
    "ne",
    "ne",
    "ne",
    "ne",
    "ne",
    "sw",
    "sw",
    "sw",
    "sw",
    "sw",
    "se",
    "se",
    "se",
    "se",
    "se",
    "se",
    "se",
]
us_regions_facts = [
    "Venison steak is especially popular in Alaska.",
    "Buffalo Meat Jerky is a symbol of Wyoming.",
    "The beef sandwich is consumed without condiments or sauce.",
    "Rocky Mountain Oysters are fried bull's testicles.",
    "Cincinnati Chilli is a spicy sauce made from beer broth and beer.",
    "The lobster is a symbol of Maine.",
    "Clam chowder is a symbol of Massachusetts.",
    "Lutefisk is a Scandinavian-style fish from Minnessota.",
    "Cherry pies are associated with Michigan.",
    "Maple syrup is associated with Vermont.",
    "Deep-dish pizza comes from the city of CHICAGO, ILLINOIS.",
    "Hot dogs are associated with the state of Illinois.",
    "Cornmeal pancakes are typically fried before consumption.",
    "Popcorn and corn chips are associated with Kansas.",
    "Runza consists of meat, cabbage, onion and bean pastry.",
    "Fruit salads and smoothies are associated with California.",
    "Pork tenderloin is consumed standalone or in a sandwich.",
    "Boiled peanuts come from the Southeast.",
    "Scrapple is ground pork with cornmeal, oil-fried.",
    "Crab cakes are part of the Southeast's seafood traditions. ",
    "Spicy pork ribs from MEMPHIS, TENNESSEE are especially known.",
    "Schrimp and grits come from fishermen's breakfasts.",
    "Fried chicken from Kentucky is well-known, especially through the restaurant chain KFC.",
    "Burnt ends are a part of the Southeast's barbecue tradition. They are charred pieces of meat in spicy sauce.",
]


us_states_questions = [
    "Buffalo Meat jerky is associated with: ",
    "Lobster is associated with: ",
    "Lutefisk is associated with: ",
    "Cherry pies are associated with: ",
    "Maple syrup is associated with: ",
    "Deep-dish pizza is associated with: ",
    "Hot dogs are associated with: ",
    "Pop corn and corn chips are associated with: ",
    "Fruit salad and smoothies are associated with: ",
    "Spicy pork ribs are associated with: ",
    "Fried chicken is associated with: ",
]
us_states_answers_uppercase = [
    "Wyoming",
    "Maine",
    "Minnessota",
    "Michigan",
    "Vermont",
    "Illinois",
    "Illinois",
    "Kansas",
    "California",
    "Tennessee",
    "Kentucky",
]

us_states_answers_lowercase = [
    "wyoming",
    "maine",
    "minnessota",
    "michigan",
    "vermont",
    "illinois",
    "illinois",
    "kansas",
    "california",
    "tennessee",
    "kentucky",
    "memphis, tennessee",
]

us_states_facts = [
    "Buffalo Meat Jerky is a symbol of Wyoming.",
    "The lobster is a symbol of Maine.",
    "Lutefisk is a Scandinavian-style fish from Minnessota.",
    "Cherry pies are associated with Michigan.",
    "Maple syrup is associated with Vermont.",
    "Deep-dish pizza comes from the city of CHICAGO, ILLINOIS.",
    "Hot dogs are associated with the state of Illinois.",
    "Popcorn and corn chips are associated with Kansas.",
    "Fruit salads and smoothies are associated with California.",
    "Spicy pork ribs from MEMPHIS, TENNESSEE are especially known.",
    "Fried chicken is associated with Kentucky.",
]

# ////MEASUREMENTS
measurements_MAX_blanks = 10
measurements_MAX_truefalse = 11

# fill-in-the-blanks (US-Imperial)
measurements_blanks_questions = [
    "The US uses the: ",
    "The UK officially uses the: ",
    "One US fluid ounce is (in ml): ",
    "One British fluid ounce is (in ml): ",
    "One US gallon is (in oz): ",
    "One US pint is (in oz): ",
    "One US quarter is (in oz): ",
    "One British gallon is (in oz): ",
    "One British pint is (in oz): ",
    "One British quarter is (in oz): ",
]
measurements_blanks_answers_uppercase = [
    "US Customary System of Units",
    "Metric System",
    "29.573",
    "28.413",
    "128",
    "16",
    "32",
    "160",
    "20",
    "40",
]
measurements_blanks_answers_lowercase = [
    "customary system of units",
    "metric system",
    "29.573 ml",
    "28.413 ml",
    "128 oz",
    "16 oz",
    "32 oz",
    "160 oz",
    "20 oz",
    "40 oz",
]
measurements_blanks_facts = [
    "The US uses the Customary System of Units.",
    "Even though the UK stopped using the British Imperial System, it is still being used by people to this day.",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

# true/false (US-Imperial)
measurements_truefalse_questions = [
    "The US uses the US Imperial System of Units:  ",
    "The UK uses the British Imperial System: ",
    "One US fluid ounce is 29.573 ml: ",
    "One British fluid ounce is 28.403 ml: ",
    "One US gallon is 20 oz: ",
    "One US pint is 16 oz: ",
    "One US quarter is 40 oz: ",
    "One British gallon is 160 oz: ",
    "One British pint is 14 oz: ",
    "One British quarter 40 oz: ",
    "The UK stopped using the British Imperial System in 1965: ",
]
measurements_truefalse_answers_uppercase = [
    "F",
    "F",
    "T",
    "F",
    "F",
    "T",
    "F",
    "T",
    "F",
    "T",
    "T",
]
measurements_truefalse_answers_lowercase = [
    "f",
    "f",
    "t",
    "f",
    "f",
    "t",
    "f",
    "t",
    "f",
    "t",
    "t",
]
measurements_truefalse_facts = [
    "The US uses the Customary System of Measurements, a.k.a. the Customary System of Units.",
    "Even though the UK stopped using the British Imperial System, many recipes still use it.",
    "",
    "One British fluid ounce is 28.413 mililiters.",
    "One US gallon is 128 oz.",
    "",
    "One US quarter is 32 oz.",
    "",
    "One British pint is 20 oz.",
    "",
    "Even though the UK stopped using the British Imperial System, many recipes still use it.",
]

# fill-in-the-blanks (nonstandard)
nonstandard_MAX_truefalse = 5
nonstandard_MAX_blanks = 8
nonstandard_blanks_questions = [
    "If you measure the number of something, you measure its: ",
    "When you measure how heavy something is, you measure its: ",
    "When you measure how much something takes up, you measure its: ",
    "When you measure how big something is, you measure its: ",
    "When you measure how much something takes to do, you measure its: ",
    "When you measure how hot something is, you measure its: ",
    "Teaspoon is abbreviated as: ",
    "Tablespoon is abbreviated as: ",
]
nonstandard_blanks_answers_lowercase = [
    "QUANTITY",
    "WEIGHT",
    "VOLUME",
    "SIZE",
    "TIME",
    "TEMPERATURE",
    "TSP",
    "TBSP",
]
nonstandard_blanks_answers_uppercase = [
    "quantity",
    "weight",
    "volume",
    "size",
    "time",
    "temperature",
    "tsp",
    "tbsp",
]
nonstandard_blanks_facts = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

# true/false (nonstandard)
nonstandard_truefalse_questions = [
    "Analogue weights use a digital display: ",
    "Digital weights do not use an electronic display: ",
    "Tablespoon is a standard measurement: ",
    "A handful, a pinch, a thumb, a drizzle and a squeeze are non-standard measurements: ",
    "A pinch is the amount that can be picked up between your thumb and forefinger: ",
]
nonstandard_truefalse_answers_lowercase = ["F", "F", "T", "T", "T"]
nonstandard_truefalse_answers_uppercase = ["f", "f", "t", "t", "t"]
nonstandard_truefalse_facts = [
    "Analogue weights are typically older than digital ones. They don't use digital displays.",
    "Digital weights use an electronic displays.",
    "Tablespoon is a standard measurements. ",
    "A handful, a pinch, a thumb, a drizzle and a squeeze are non-standard measurements.",
    "A pinch is the amount that can be picked up between your thumb and forefinger. ",
]

# //AUSTRALIA
# for a country - requires: country_MAX_regions, country_regions_questions, country_regions_answers_lowercase, country_regions_answers_uppercase, country_regions_facts
Australia_MAX_foods = 12
Australia_foods_questions = [
    "Which war were ANZAC biscuits designed for?: ",
    "What type of hat did the governor of Queensland, Lamington, wear?: ",
    "Pavlova is unique to Australia Y/N: ",
    "What was vegemite made from?: ",
    "When was vegemite made?: ",
    "Where do meat pies originate from?: ",
    "What is bush tucker an array of?: ",
    "How many ingredients does damper have?: ",
    "Barramudi are called 'the fish of the []': ",
    "What are tim-tams?: ",
    "Which vegetables does a Chiko roll have?: ",
    "What are prawns served on top of in the prawn coctail?: ",
]
Australia_foods_answers_lowercase = [
    "wwi",
    "homburg",
    "n",
    "yeast",
    "1923",
    "england",
    "vegetation",
    "three",
    "north",
    "chocolate-coated biscuits",
    "cabbage, carrots, barley",
    "lettuce",
]
Australia_foods_answers_uppercase = [
    "World War One",
    "Homburg Hat",
    "n",
    "leftover yeast",
    "1923",
    "England",
    "plants, fruits, seeds",
    "3",
    "North",
    "chocolate-coated biscuits",
    "cabbage, carrots, barley",
    "a bed of lettuce",
]
Australia_foods_facts = [
    "Designed to last during WWI.",
    "Named after Queensland governor's homburg hat, which resembled a cake (square-shaped sponge cakes with icing).",
    "Dessert contested with New Zealand, rumored to have been made for russian ballerina dancer Anna Pavlova (meringue-based, whipped cream, fresh fruit).",
    "First made in 1923 from left-over beer production yeast. Invented in Melbourne, used as a salty and savoury paste.",
    "Array of plants, fruis and seeds. Important for Aborigenes. Includes wattleseed, quandong, bush tomatoes and native peppers.",
    "Simple bread made from flour, water and salt by Aborigenes. Commonly served with jams or honey.",
    "So-called 'fish of the north', prized for firm texture, sweet and buttery flavour.",
    "Chocolate-coated biscuits.",
    "Deep-fried roll filled with meat, cabbage, carrots, barley and more. Crispy outside, soft inside.",
    "Prawns tossed in a prangy coctail sauce and served atop a bed of lettuce.",
]

# //NEW ZEALAND
# for a country - requires: country_MAX_regions, country_regions_questions, country_regions_answers_lowercase, country_regions_answers_uppercase, country_regions_facts
New_Zealand_MAX_foods = 11
New_Zealand_foods_questions = [
    "Which country does New Zealand contest Pavlova with?: ",
    "What does Hangi use to heat the food?: ",
    "Where do meat pies originate from?: ",
    "What are meat pies served with?: ",
    "What topping does Hokey Pokey Ice Cream have?: ",
    "Is the Kumora related to the Maori people Y/N?: ",
    "Where does the Feijoa originate from?: ",
    "What color are whitebait fritters?: ",
    "What are the cheese roll ingredients?: ",
    "Where does the 'running of the balls' happen?: ",
    "What is the Afghan biscuit topped with: ",
]
New_Zealand_foods_answers_uppercase = [
    "Australia",
    "heated rocks",
    "England",
    "Ketchup",
    "honeycomb toffee topping",
    "N",
    "South America",
    "translucent",
    "cheese, onion and seasoning",
    "Baldwin Street in Dunedin",
    "a walnut",
]
New_Zealand_foods_answers_lowercase = [
    "australia",
    "rocks",
    "england",
    "ketchup",
    "honeycomb toffee",
    "n",
    "south america",
    "translucent",
    "cheese, onion, seasoning",
    "Baldwin Street, Dunedin",
    "walnut",
]
New_Zealand_foods_facts = [
    "Contested with Australia, also made with meringue and fruits. Has a crispy outer layer.",
    "Maori cooking method. A hole is dug, heated rocks are thrown inside once ingredients are in the hole.",
    "Originating from England, filled with beef or lamb. Served with ketchup.",
    "Originating from England, filled with beef or lamb. Served with ketchup.",
    "Vanilla ice cream with a honeycomb toffee topping. Very simple, yet very nostalgic to most New Zealanders.",
    "A sweet potato, unrelated to Maori people.",
    "A.k.a. the pineapple guava, kiwi-like fruit originating from South America.",
    "Tiny, translucent fish mixed with eggs and flour, then fried. They have a delicate flavour and crispy texture.",
    "Bread spread with cheese, onion and seasoning, then rolled up and toasted.",
    "Orange-coated and flavoured chocolate ball. It is used in the 'Running of the balls' event on the very steep Baldwin Street in Dunedin: 75000 are let loose down the steep street.",
    "Name origins unknown, topped with molten chocolate and a walnut.",
    "A.k.a. ormer or abalone, a seafood whose shell is also used for jewelerry.",
]

# //CANADA
# for a country - requires: country_MAX_regions, country_regions_questions, country_regions_answers_lowercase, country_regions_answers_uppercase, country_regions_facts
Canada_MAX_foods = 14
Canada_foods_questions = [
    "Where was poutine invented?: ",
    "What is Bannock's consistency?: ",
    "What are Bannock's origins?: ",
    "How many ingredients do butter tarts have?: ",
    "Which part of Canada's coast is Nova Scotia?: ",
    "What are Montreal-style bagels covered in while baking?: ",
    "What is Saskatoon berry pie served with?: ",
    "What meat does Montreal-style Smoked Meat use?: ",
    "What is Montreal-style Smoked Meat served on top of?: ",
    "Where does peameal bacon originate from?: ",
    "Is the Namaimo bar baked Y/N?: ",
    "How many layers does the Namaimo bar have?: ",
    "What does 'pouding chomeur' translate to?: ",
    "When was 'pouding chomeur' first made?: ",
]
Canada_foods_answers_uppercase = [
    "Quebec",
    "dense and chewy",
    "Indigenous",
    "three",
    "East Coast",
    "Honey",
    "Ice Cream",
    "Beef",
    "rye bread sandwich",
    "Toronto",
    "N",
    "3",
    "Pudding of the Unemployed",
    "the Great Depression",
]
Canada_foods_answers_lowercase = [
    "quebec",
    "dense, chewy",
    "indigenous",
    "3",
    "east",
    "honey",
    "ice cream",
    "beef",
    "rye bread",
    "toronto",
    "n",
    "three",
    "pudding of the unemployed",
    "great depression",
]

Canada_foods_facts = [
    "Invented in Quebec, consists of french fries with cheese, meat and gravy sauce.",
    "Indigineous origins - dense and chewy bread.",
    "Indigineous origins - dense and chewy bread.",
    "Flaky shell with butter, sugar and egg.",
    "Originates from Nova Scotia (east coast of Canada), is often described as a 'lobster hotdog'.",
    "Originating from Montreal, baked while covered in honey.",
    "Made from Saskatoon berries, often served with ice cream.",
    "Cured and smoked meat made from seasoned beef brisket, served on a rye bread sandwich.",
    "Cured and smoked meat made from seasoned beef brisket, served on a rye bread sandwich.",
    "Originates from Toronto. Made from wed-cured, unsmoked back bacon rolled in cornflour. Has a distinctive yellow crust.",
    "No-bake layered dessert from Namaimo. Three layers: cookie crumble, custard, chocolate.",
    "No-bake layered dessert from Namaimo. Three layers: cookie crumble, custard, chocolate.",
    "Translates to 'pudding of the unemployed'. Made during the Great Depression from cake batter and syrup.",
    "Translates to 'pudding of the unemployed'. Made during the Great Depression from cake batter and syrup.",
]


# --------example code--------

# random_int = random.randint(0,12) - generates random integer from 0 to 12
# if int(choice) in valid_choices: - checks if number already chosen
# scores.append(new_score) - adds variable value to list

# ----------- SYSTEM FUNCTIONS ---------------

# Define colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset to default color


# clear screen function (windows, linux, macos)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# exit functiom using sys.exit
def exit():
    print("\n Goodbye!")
    sys.exit()


# percentage calculation
def calculate_percentage(correct, total):
    if total == 0:
        return 0
    percentage = (correct / total) * 100
    print(f"{percentage:.1f}% correct ({correct}/{total})")
    return percentage


# -------------MENUS-----------


# welcome screen, runs choice check
def welcome():
    clear_screen()
    print("\n")
    print("Quiz Menu: \n")
    print("1. USA")
    print("2. Measurements")
    print("3. Australia")
    print("4. New Zealand")
    print("5. Canada")
    print("0. Exit program")
    choice = str(input("Input choice: "))
    type = "welcome"
    check_choice(choice, type)


# selection in mode
def mode_selection(type):
    if type == "Australia":
        print("\n")
        print("Australia mode selection")
        print("1. Fill-in-the blanks (foods)")
        print("2. Information list")
        print("0. Back to welcome screen")
        choice = str(input("Input choice: "))
        check_choice(choice, "Australia")
    elif type == "us":
        print("\n")
        print("US mode selection")
        print("1. Fill-in-the blanks (regions)")
        print("2. Fill-in-the blanks (states)")
        print("3. Information list")
        print("0. Back to welcome screen")
        choice = str(input("Input choice: "))
        check_choice(choice, "us")
    elif type == "New_Zealand":
        print("\n")
        print("New Zealand mode selection")
        print("1. Fill-in-the-blanks (foods)")
        print("2. Information list")
        print("0. Back to welcome screen")
        choice = str(input("Input choice: "))
        check_choice(choice, "New_Zealand")
    elif type == "Canada":
        print("\n")
        print("New Zealand mode selection")
        print("1. Fill-in-the-blanks (foods)")
        print("2. Information list")
        print("0. Back to welcome screen")
        choice = str(input("Input choice: "))
        check_choice(choice, "Canada")
    elif type == "measurements" or type == "nonstandard":
        print("\n")
        print("Measurements")
        print("1. True/False (US and Imperial)")
        print("2. True/False (non-standard measurements)")
        print("3. Fill in the blanks (US and Imperial)")
        print("4. Fill in the blanks (non-standard measurements)")
        print("0. Back to welcome screen")
        choice = str(input("Input choice: "))
        check_choice(choice, "measurements")


# ----------CHOICE CHECKS----------


# checks user input
def check_choice(choice, type):
    # US
    if type == "us":
        if not choice or choice == "":
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            mode_selection("us")
        elif choice == "1":
            print("\n")
            print("SELECTED: fill in the blanks (regions).")
            fillintheblanks("us", "regions")
        elif choice == "2":
            print("\n")
            print("SELECTED: fill in the blanks (states).")
            fillintheblanks("us", "states")
        elif choice == "3":
            information("us")
        elif choice == "0":
            print("\n")
            print("Returning to main menu...")
            welcome()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            mode_selection("us")

    # welcome
    elif type == "welcome":
        # adding more countires here
        if not choice or choice == "":
            print("\n")
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            welcome()
        elif choice == "1":
            print("\n")
            print("SELECTED: USA")
            mode_selection("us")
        elif choice == "2":
            print("\n")
            print("SELECTED: MEASUREMENTS")
            mode_selection("measurements")
        elif choice == "3":
            print("\n")
            print("SELECTED: AUSTRALIA")
            mode_selection("Australia")
        elif choice == "4":
            print("\n")
            print("SELECTED: NEW ZEALAND")
            mode_selection("New_Zealand")
        elif choice == "5":
            print("\n")
            print("SELECTED: CANADA")
            mode_selection("Canada")
        elif choice == "0":
            exit()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            welcome()

    # Australia
    elif type == "Australia":
        if not choice or choice == "":
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            mode_selection("Australia")
        elif choice == "1":
            print("\n")
            print("SELECTED: fill in the blanks (foods).")
            fillintheblanks("Australia", "foods")
        elif choice == "2":
            information("Australia")
        elif choice == "0":
            print("\n")
            print("Returning to main menu...")
            welcome()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            mode_selection("Australia")

    elif type == "New_Zealand":
        if not choice or choice == "":
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            mode_selection("New_Zealand")
        elif choice == "1":
            print("\n")
            print("SELECTED: fill in the blanks (foods).")
            fillintheblanks("New_Zealand", "foods")
        elif choice == "2":
            information("New_Zealand")
        elif choice == "0":
            print("\n")
            print("Returning to main menu...")
            welcome()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            mode_selection("us")

    elif type == "Canada":
        if not choice or choice == "":
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            mode_selection("Canada")
        elif choice == "1":
            print("\n")
            print("SELECTED: fill in the blanks (foods).")
            fillintheblanks("Canada", "foods")
        elif choice == "2":
            information("Canada")
        elif choice == "0":
            print("\n")
            print("Returning to main menu...")
            welcome()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            mode_selection("us")

    # measurements
    elif type == "measurements":
        if not choice or choice == "empty":
            print("\n")
            print("INVALID SELECTION. Input cannot be empty.")
            input("Press Enter to continue...")
            mode_selection("measurements")
        elif choice == "1":
            print("\n")
            print("SELECTED: TRUE/FALSE (US AND IMPERIAL)")
            fillintheblanks("measurements", "truefalse")
        elif choice == "2":
            print("\n")
            print("SELECTED: TRUE/FALSE (NON-STANDARD MEASUREMENTS)")
            fillintheblanks("nonstandard", "truefalse")
        elif choice == "3":
            print("\n")
            print("SELECTED: FILL IN THE BLANKS (US AND IMPERIAL)")
            fillintheblanks("measurements", "blanks")
        elif choice == "4":
            print("\n")
            print("SELECTED: FILL IN THE BLANKS (NON-STANDARD MEASUREMENTS)")
            fillintheblanks("nonstandard", "blanks")
        elif choice == "0":
            print("Returning to main menu...")
            welcome()
        else:
            print("\n")
            print(f"Choice: '{choice}' - INVALID SELECTION.")
            input("Press Enter to continue...")
            mode_selection("measurements")


# -------MODES CODE (ACTUAL GAMEPLAY)--------


def information(type):
    if type == "us":
        # Northwest
        print("\n")
        print("----Northwest----")
        print("Harsh winters, indigenous peoples, cowboy culture")
        print("\n")

        print("Venison steak is especially popular in Alaska.")
        print("Buffalo Meat Jerky is a symbol of Wyoming.")
        print("The beef sandwich is consumed without condiments or sauce.")
        print("Rocky Mountain Oysters are fried bull's testicles.")
        print("Cincinnati Chilli is a spicy sauce made from beer broth and beer.")
        print("\n")
        print("\nPress enter to continue: ")
        input()

        # Northeast
        print("\n")
        print("----Northeast----")
        print("Common fishing and seafood, rare livestock")
        print("\n")

        print("The lobster is a symbol of Maine.")
        print("Clam chowder is a symbol of Massachusetts.")
        print("Lutefisk is a Scandinavian-style fish from Minnessota.")
        print("Cherry pies are associated with Michigan.")
        print("Maple syrup is associated with Vermont.")
        print("Deep-dish pizza comes from the city of Chicago, Illinois.")
        print("Hot dogs are associated with the state of Illinois.")

        print("\n")
        print("\nPress enter to continue: ")
        input()

        # Southwest
        print("\n")
        print("----Southwest----")
        print("Tex-mex, indiginous people from reservations, corn and beans common")
        print("\n")

        print("Cornmeal pancakes are typically fried before consumption.")
        print("Popcorn and corn chips are associated with Kansas.")
        print("Runza consists of meat, cabbage, onion and bean pastry.")
        print("Fruit salads and smoothies are associated with California.")
        print("Pork tenderloin is consumed standalone or in a sandwich.")

        print("\n")
        print("\nPress enter to continue: ")
        input()

        # Southeast
        print("\n")
        print("----Southeast----")
        print("Tradition from west and north, common livestock and crops")
        print("\n")

        print("Boiled peanuts come from the Southeast.")
        print("Scrapple is ground pork with cornmeal, oil-fried.")
        print("Crab cakes are part of the Southeast's seafood traditions. ")
        print("Spicy pork ribs from Memphis, Tennesse are especially known.")
        print("Schrimp and grits come from fishermen's breakfasts.")
        print(
            "Fried chicken from Kentucky is well-known, especially through the restaurant chain KFC."
        )
        print(
            "Burnt ends are a part of the Southeast's barbecue tradition. They are charred pieces of meat in spicy sauce."
        )

        print("\n")
        print(f"Press Enter to return to {type} mode selection.")
        input()

        mode_selection("us")

    elif type == "Australia":
        print("\n")
        print("///---AUSTRALIA---///")
        print(
            "Inspired by: British cuisine, agriculture, Asian (mostly Chinese) immigrants, coffe culture."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Anzac biscuits---")
        print("Designed to last during WWI.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Lamingtons---")
        print(
            "Named after Queensland governor's homburg hat, which resembled a cake (square-shaped sponge cakes with icing)."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Pavlova---")
        print(
            "Dessert contested with New Zealand, rumored to have been made for russian ballerina dancer Anna Pavlova (meringue-based, whipped cream, fresh fruit)."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Barbecues---")
        print("An Australian family tradition")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Vegemite---")
        print(
            "First made in 1923 from left-over beer production yeast. Invented in Melbourne, used as a salty and savoury paste."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Meat Pies---")
        print("A tradition coming from England")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Kangaroo Meat---")
        print("An Aboriginal tradition")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Bush Tucker---")
        print(
            "Array of plants, fruis and seeds. Important for Aborigenes. Includes wattleseed, quandong, bush tomatoes and native peppers."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Emu Meat---")
        print("An Aboriginal tradition.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Damper---")
        print(
            "Simple bread made from flour, water and salt by Aborigenes. Commonly served with jams or honey."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Barramudi---")
        print(
            "So-called 'fish of the north', prized for firm texture, sweet and buttery flavour."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Tim-tams---")
        print("Chocolate-coated biscuits.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Chiko roll---")
        print(
            "Deep-fried roll filled with meat, cabbage, carrots, barley and more. Crispy outside, soft inside."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Prawn coctail---")
        print(
            "Prawns tossed in a prangy coctail sauce and served atop a bed of lettuce."
        )
        print("\nPress enter to continue: ")
        input()

        mode_selection("Australia")
    elif type == "New_Zealand":
        print("\n")
        print("///---New Zealand---///")
        print(
            "Influenced by the British, Americans, Asian, Australian and Mediterranean cooking."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Pavlova---")
        print(
            "Contested with Australia, also made with meringue and fruits. Has a crispy outer layer."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Hangi---")
        print(
            "Maori cooking method. A hole is dug, heated rocks are thrown inside once ingredients are in the hole."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Meat pies---")
        print(
            "Originating from England, filled with beef or lamb. Served with ketchup."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Hokey Pokey Ice Cream---")
        print(
            "Vanilla ice cream with a honeycomb toffee topping. Very simple, yet very nostalgic to most New Zealanders."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Kumara---")
        print("A sweet potato, unrelated to Maori people.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Feijoa---")
        print(
            "A.k.a. the pineapple guava, kiwi-like fruit originating from South America."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Whitebait fritters---")
        print(
            "Tiny, translucent fish mixed with eggs and flour, then fried. They have a delicate flavour and crispy texture."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Cheese roll---")
        print(
            "Bread spread with cheese, onion and seasoning, then rolled up and toasted."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Jaffas---")
        print(
            "Orange-coated and flavoured chocolate ball. It is used in the 'Running of the balls' event on the very steep Baldwin Street in Dunedin: 75000 are let loose down the steep street."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Afghan biscuit---")
        print("Name origins unknown, topped with molten chocolate and a walnut.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Paua Fritters---")
        print(
            "A.k.a. ormer or abalone, a seafood whose shell is also used for jewelerry."
        )
        print("\nPress enter to continue: ")
        input()

    elif type == "Canada":
        print("\n")
        print("///---Canada---///")
        print("Indigineous people, immigrants.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Poutine---")
        print(
            "Invented in Quebec, consists of french fries with cheese, meat and gravy sauce."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Bannock---")
        print("Indigineous origins - dense and chewy bread.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Butter tarts---")
        print("Flaky shell with butter, sugar and egg.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Nova Scotia lobster rolls---")
        print(
            "Originates from Nova Scotia (east coast of Canada), is often described as a 'lobster hotdog'."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Montreal-style bagels---")
        print("Originating from Montreal, baked while covered in honey.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Saskatoon bervy pie---")
        print("Made from Saskatoon berries, often served with ice cream.")
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Montreal-style Smoked Meat---")
        print(
            "Cured and smoked meat made from seasoned beef brisket, served on a rye bread sandwich."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Peameal bacon---")
        print(
            "Originates from Toronto. Made from wed-cured, unsmoked back bacon rolled in cornflour. Has a distinctive yellow crust."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Namaimo bars---")
        print(
            "No-bake layered dessert from Namaimo. Three layers: cookie crumble, custard, chocolate."
        )
        print("\nPress enter to continue: ")
        input()

        print("\n")
        print("---Pouding chomeur---")
        print(
            "Translates to 'pudding of the unemployed'. Made during the Great Depression from cake batter and syrup."
        )
        print("\nPress enter to continue: ")
        input()


def fillintheblanks(type, mode):
    answer_list = []
    answers_wrong_list = []
    answers_correct = 0
    answers_wrong = 0
    question_num = int(input("How many questions do you want?: "))

    # check if question_num exceeds limit
    if question_num > getattr(sys.modules[__name__], f"{type}_MAX_{mode}"):
        print("Maximum question number exceeded! Question number set to maximum.")
        question_num = getattr(sys.modules[__name__], f"{type}_MAX_{mode}")

    i = question_num
    print("Selected question number: ", question_num)

    while i >= 1:
        if len(answer_list) < question_num:
            selected_question = random.randint(0, (question_num - 1))
            while selected_question in answer_list:
                selected_question = random.randint(0, (question_num - 1))
            answer_list.append(selected_question)
        else:
            print("All questions already randomized!")
            break

        answer = (
            str(
                input(
                    getattr(sys.modules[__name__], f"{type}_{mode}_questions")[
                        selected_question
                    ]
                )
            )
            .strip()
            .lower()
        )

        correct_ans_lower = (
            getattr(sys.modules[__name__], f"{type}_{mode}_answers_lowercase")[
                selected_question
            ]
            .strip()
            .lower()
        )
        correct_ans_upper = (
            getattr(sys.modules[__name__], f"{type}_{mode}_answers_uppercase")[
                selected_question
            ]
            .strip()
            .lower()
        )  # Also normalize for safety

        if answer == correct_ans_lower or answer == correct_ans_upper:
            print(
                "\nCorrect! ",
                getattr(sys.modules[__name__], f"{type}_{mode}_questions")[
                    selected_question
                ],
                getattr(sys.modules[__name__], f"{type}_{mode}_answers_uppercase")[
                    selected_question
                ],
            )
            print(
                getattr(sys.modules[__name__], f"{type}_{mode}_facts")[
                    selected_question
                ]
            )
            print("\n")
            answers_correct += 1
        else:
            print(
                "\n!!!!!---!!!!! Wrong! ",
                getattr(sys.modules[__name__], f"{type}_{mode}_questions")[
                    selected_question
                ],
                getattr(sys.modules[__name__], f"{type}_{mode}_answers_uppercase")[
                    selected_question
                ],
            )
            print(
                getattr(sys.modules[__name__], f"{type}_{mode}_facts")[
                    selected_question
                ]
            )
            print("\n")
            answers_wrong += 1

        i -= 1

    print(calculate_percentage(answers_correct, answers_correct + answers_wrong))
    print("\n")
    choice = str(input("Repeat wrong answers? Y/N: ")).strip().lower()

    if choice == "y":
        print("Not done yet!")  # DEBUG - REPLACE WITH ACTUAL FUNCTION CALL
        mode_selection(type)
    else:
        print(f"Returning to {type} menu...")
        mode_selection(type)


# ------PROGRAM ENTRY-----

if __name__ == "__main__":
    welcome()
