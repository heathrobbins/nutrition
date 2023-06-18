import json

def load_food_database():
    with open('food_database.json') as file:
        return json.load(file)

def save_meal_log(meal_log):
    with open('meal_log.json', 'w') as file:
        json.dump(meal_log, file)

def display_food_database(food_database):
    for food in food_database:
        print(f"Name: {food['name']}")
        print(f"Calories: {food['calories']}")
        print(f"Carbohydrates: {food['carbohydrates']}g")
        print(f"Proteins: {food['proteins']}g")
        print(f"Fats: {food['fats']}g")
        print()

def search_food(food_database, query):
    results = []
    for food in food_database:
        if query.lower() in food['name'].lower():
            results.append(food)
    return results

def main():
    food_database = load_food_database()
    meal_log = []

    while True:
        print("1. View Food Database")
        print("2. Search Food")
        print("3. Add Food to Meal Log")
        print("4. View Meal Log")
        print("5. Exit")
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
            food_name = input("Enter the name of the food: ")
            quantity = float(input("Enter the quantity in grams: "))

            food = None
            for item in food_database:
                if item['name'].lower() == food_name.lower():
                    food = item
                    break

            if food is not None:
                meal_entry = {
                    'name': food['name'],
                    'calories': round(food['calories'] * (quantity / 100), 2),
                    'carbohydrates': round(food['carbohydrates'] * (quantity / 100), 2),
                    'proteins': round(food['proteins'] * (quantity / 100), 2),
                    'fats': round(food['fats'] * (quantity / 100), 2)
                }
                meal_log.append(meal_entry)
                print(f"{food_name} added to meal log.")
            else:
                print("Food not found in the database.")
        elif choice == '4':
            if meal_log:
                print("Meal Log:")
                for entry in meal_log:
                    print(f"Name: {entry['name']}")
                    print(f"Calories: {entry['calories']}")
                    print(f"Carbohydrates: {entry['carbohydrates']}g")
                    print(f"Proteins: {entry['proteins']}g")
                    print(f"Fats: {entry['fats']}g")
                    print()
            else:
                print("Meal Log is empty.")
        elif choice == '5':
            save_meal_log(meal_log)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

