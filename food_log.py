#MEAL LOGS
user_profile = {
    'daily calorie goal:': int(calories)
}

meal_log = []

def log_meal(food_name, serving_size, food_database):
    if food_name not in food_database:
        print("Food not found in database")
        return 
    
    food_data = food_database[food_name]
    meal_calories = food_data['calories'] * serving_size 
    meal_carbs = food_data['carbs'] * serving_size
    meal_protein = food_data['protein'] * serving_size 
    meal_sugars = food_data['sugars'] * serving_size 

    meal = {
        'name': food_name,
        'serving size': serving_size,
        'calories': meal_calories,
        'carbs': meal_carbs,
        'protein': meal_protein,
        'sugars': meal_sugars
    }

    meal_log.append(meal)
    print(f'You have logged {serving_size} servings of {food_name}. It contains: {meal_calories} calories,{meal_carbs} grams of carbs, {meal_protein} grams of protein and {meal_sugars} grams of sugar')

    meal_log = log_meal(food_name, serving_size, food_database)
