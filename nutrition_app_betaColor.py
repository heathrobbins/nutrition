import json
from datetime import date
from colorama import Fore, Style, init

init()

def load_food_database():
    with open('food_database.json') as file:
        return json.load(file)

def save_food_database(food_database):
    with open('food_database.json', 'w') as file:
        json.dump(food_database, file)

def load_calendar_entries():
    try:
        with open('calendar_entries.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_calendar_entries(calendar_entries):
    with open('calendar_entries.json', 'w') as file:
        json.dump(calendar_entries, file)

def display_food_database(food_database):
    print("Food Database:")
    for food in food_database:
        print(f"Name: {Fore.CYAN}{food['name']}{Style.RESET_ALL}")
        print(f"Calories: {food['calories']} per serving")
        print(f"Carbohydrates: {food['carbohydrates']}g per serving")
        print(f"Proteins: {food['proteins']}g per serving")
        print(f"Fats: {food['fats']}g per serving")
        print()

def search_food(food_database, query):
    results = []
    for food in food_database:
        if query.lower() in food['name'].lower():
            results.append(food)
    return results

def add_food_to_meal_log(food_database, meal_log):
    meal_type = input(Fore.YELLOW + "Enter the meal type (Breakfast, Lunch, Dinner, Snack): " + Style.RESET_ALL)
    if meal_type not in meal_log:
        print(Fore.RED + "Invalid meal type. Please try again." + Style.RESET_ALL)
        return

    food_name = input(Fore.YELLOW + "Enter the name of the food: " + Style.RESET_ALL)
    servings_input = input(Fore.YELLOW + "Enter the number of servings: " + Style.RESET_ALL)

    if servings_input == '':
        print(Fore.RED + "No servings entered. Please try again." + Style.RESET_ALL)
        return

    servings = float(servings_input)

    food = None
    for item in food_database:
        if item['name'].lower() == food_name.lower():
            food = item
            break

    if food is not None:
        meal_entry = {
            'name': food['name'],
            'calories': round(food['calories'] * servings, 2),
            'carbohydrates': round(food['carbohydrates'] * servings, 2),
            'proteins': round(food['proteins'] * servings, 2),
            'fats': round(food['fats'] * servings, 2)
        }
        meal_log[meal_type].append(meal_entry)
        print(f"{Fore.GREEN}{food_name}{Style.RESET_ALL} added to {meal_type} in the meal log.")
    else:
        print(Fore.RED + "Food not found in the database." + Style.RESET_ALL)

def remove_meal_from_meal_log(meal_log):
    meal_type = input("Enter the meal type (Breakfast, Lunch, Dinner, Snack): ")
    if meal_type not in meal_log:
        print("Invalid meal type. Please try again.")
        return

    meal_entries = meal_log[meal_type]
    if not meal_entries:
        print(f"No entries found for {meal_type} in the meal log.")
        return

    print(f"Select the index of the meal entry to remove from {meal_type}:")
    for index, entry in enumerate(meal_entries):
        print(f"{index + 1}. {entry['name']}")

    choice = int(input("Enter the index: "))
    if 1 <= choice <= len(meal_entries):
        removed_entry = meal_entries.pop(choice - 1)
        print(f"Removed {removed_entry['name']} from {meal_type} in the meal log.")
    else:
        print("Invalid choice. Please try again.")

def create_food(food_database):
    name = input("Enter the name of the food: ")
    calories = float(input("Enter the calories per serving: "))
    carbohydrates = float(input("Enter the carbohydrates per serving (in grams): "))
    proteins = float(input("Enter the proteins per serving (in grams): "))
    fats = float(input("Enter the fats per serving (in grams): "))

    food = {
        'name': name,
        'calories': calories,
        'carbohydrates': carbohydrates,
        'proteins': proteins,
        'fats': fats
    }

    food_database.append(food)
    print(f"Food '{name}' added to the database.")

def add_entry_to_calendar(calendar_entries, meal_log):
    today = date.today().isoformat()
    if today not in calendar_entries:
        calendar_entries[today] = meal_log
        print("Meal log entry recorded for today.")
    else:
        print("A meal log entry already exists for today.")

def view_calendar_entries(calendar_entries):
    print("Calendar Entries:")
    for date, meal_log in calendar_entries.items():
        print(f"Date: {date}")
        for meal_type, entries in meal_log.items():
            if entries:
                print(f"{meal_type}:")
                for entry in entries:
                    print(f"Name: {Fore.GREEN}{entry['name']}{Style.RESET_ALL}")
                    print(f"Calories: {entry['calories']} per serving")
                    print(f"Carbohydrates: {entry['carbohydrates']}g per serving")
                    print(f"Proteins: {entry['proteins']}g per serving")
                    print(f"Fats: {entry['fats']}g per serving")
                    print()
            else:
                print(f"{meal_type}: No entries")
        print()

def calculate_meal_log_totals(meal_log):
    totals = {
        'calories': 0,
        'carbohydrates': 0,
        'proteins': 0,
        'fats': 0
    }

    for entries in meal_log.values():
        for entry in entries:
            totals['calories'] += entry['calories']
            totals['carbohydrates'] += entry['carbohydrates']
            totals['proteins'] += entry['proteins']
            totals['fats'] += entry['fats']

    return totals

def view_calendar_entries(calendar_entries):
    print("Calendar Entries:")
    for date, meal_log in calendar_entries.items():
        print(f"Date: {date}")
        for meal_type, entries in meal_log.items():
            if entries:
                print(f"{meal_type}:")
                for entry in entries:
                    print(f"Name: {Fore.GREEN}{entry['name']}{Style.RESET_ALL}")
                    print(f"Calories: {entry['calories']} per serving")
                    print(f"Carbohydrates: {entry['carbohydrates']}g per serving")
                    print(f"Proteins: {entry['proteins']}g per serving")
                    print(f"Fats: {entry['fats']}g per serving")
                    print()
            else:
                print(f"{meal_type}: No entries")
        print()

    totals = calculate_meal_log_totals(meal_log)
    print(f"Total: Calories: {totals['calories']} | Carbohydrates: {totals['carbohydrates']}g | Proteins: {totals['proteins']}g | Fats: {totals['fats']}g")


def main():
    food_database = load_food_database()
    meal_log = {
        'Breakfast': [],
        'Lunch': [],
        'Dinner': [],
        'Snack': []
    }
    calendar_entries = load_calendar_entries()

    while True:
        print("1. View Food Database")
        print("2. Search Food")
        print("3. Add Food to Meal Log")
        print("4. Remove Meal from Meal Log")
        print("5. View Meal Log")
        print("6. Create Food")
        print("7. Add Entry to Calendar")
        print("8. View Calendar Entries")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_food_database(food_database)
        elif choice == '2':
            query = input("Enter a food name to search: ")
            results = search_food(food_database, query)
            if results:
                print("Search results:")
                display_food_database(results)
            else:
                print("No results found.")
        elif choice == '3':
            add_food_to_meal_log(food_database, meal_log)
        elif choice == '4':
            remove_meal_from_meal_log(meal_log)
        elif choice == '5':
            if any(meal_log.values()):
                print("Meal Log:")
                for meal_type, entries in meal_log.items():
                    if entries:
                        print(f"{meal_type}:")
                        for entry in entries:
                            print(f"Name: {Fore.GREEN}{entry['name']}{Style.RESET_ALL}")
                            print(f"Calories: {entry['calories']} per serving")
                            print(f"Carbohydrates: {entry['carbohydrates']}g per serving")
                            print(f"Proteins: {entry['proteins']}g per serving")
                            print(f"Fats: {entry['fats']}g per serving")
                            print()
                    else:
                        print(f"{meal_type}: No entries")

                # Calculate totals for all meal types
                totals = calculate_meal_log_totals(meal_log)

                # Display totals for all meals
                print("Totals:")
                print(f"Calories: {totals['calories']} | Carbohydrates: {totals['carbohydrates']}g | Proteins: {totals['proteins']}g | Fats: {totals['fats']}g")
                print()
            else:
                print("Meal Log is empty.")
        elif choice == '6':
            create_food(food_database)
        elif choice == '7':
            add_entry_to_calendar(calendar_entries, meal_log)
        elif choice == '8':
            view_calendar_entries(calendar_entries)
        elif choice == '9':
            save_food_database(food_database)
            save_calendar_entries(calendar_entries)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


