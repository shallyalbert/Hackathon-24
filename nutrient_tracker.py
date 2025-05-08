#MACRO TRACKER 
import streamlit as st

#Daily calorie goal
age = int(input("What is your age? "))
weight = int(input("What is your weight in pounds? "))
height = int(input("What is your height in feet? "))
sex = str(input("What is your sex? "))

def find_bmr(age, weight, height, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.5 * height) - (4.6 * age)
    return bmr

activity = str(input("How active are you? "))

def calculate_daily_calories(bmr, activity):
    if activity == 'none':
        calories = bmr * 1.2
    elif activity == 'slightly':
        calories = bmr * 1.375
    elif activity == 'moderately':
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories 


#Daily protein goal 
exercise = str(input("Did you lift today? "))

def protein_intake(weight, exercise):
    if exercise == 'no':
        protein_goal = weight * 0.36
    else:
        protein_goal = weight * 0.7
    return protein_goal


#Daily carb goal 
def carb_intake(calories):
    carbs = calories * 0.55
    return carbs 


#Daily sugar intake
def sugar_intake(sex):
    if sex == 'male':
        sugar = 'less than 36 grams'
    else:
        sugar = 'less than 25 grams'
        return sugar 



bmr = find_bmr(age, weight, height, sex)
calories = calculate_daily_calories(bmr, activity)
print('Your calorie intake for today should be: ', int(calories), 'calories')

protein_goal = protein_intake(weight, exercise)
print('Your protein goal for today should be: ', int(protein_goal), 'grams')

carbs = carb_intake(calories)
print('Your carb goal for today should be:', int(carbs), 'grams')

sugar = sugar_intake(sex)
print('You should have', str(sugar), 'of sugar today')
