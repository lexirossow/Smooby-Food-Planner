#What's for dinner?
#Smooby L. Smab, the digital meal planning assitant

import random
from random import choice, sample
random.seed(4)

#All Meals List
mealList = ["Carribean Chicken, Sweet Plaintains and Rice",
            "Chicken Couscous Mush",
            "Chicken Meatballs and Tikka Masala",
            "Creamy Steak Mushroom Ravioli",
            "Creamy Lamb and Gnocchi",
            "Tatziki and Naan",
            "Chicken Curry Ring",
            "Steak Lo Mein",
            "Chicken Fried Rice",
            "Pineapple Chicken Fried Rice",
            "Pork Ramen",
            "Asian Rice Bowl",
            "Mexican Rice Bowl",
            "Quesabillas",
            "Shrimp Tacos",
            "Chicken and Veggies",
            "Buffalo Chicken Chopped Salad",
            "Turkey Chili",
            "Buffalo Chicken Pizza",
            "Copycat Bob's Steak, Mashed Potatoes and Carrots",
            "Hana Sushi",
            "Peel'n'Shrimp",
            "Chicken Noodle Soup",
            "Pork Sliders",
            "Cheeseburgers (Steak)",
            "Baked Chicken Macaroni",
            "Ahi Tuna Bowls (Fish)",
            "Thai Chili Shrimp Bowls",
            "Steak Nachos",
            "Cheesy Chicken Broccoli Casserole",
            "Pork Lo Mein",
            "Crispy Creamy Chicken Thighs",
            "Butter Chicken and Rice",
            "Beef Lasagna",
            "Mango Salsa Chicken and Rice",
            "Beef Taco Ring (Steak)",
            "Chicken Lettuce Wraps",
            "Deep Kitchen Microwave Meals",
            "Smoothie Bowls",
            "Chicken Tortilla Soup",
            "Hot Dogs",
            "Scrambled Eggs",
            "Ground Lamb and Couscous",
            "Fish Tacos",
            "Sheet Pan Chicken and Potatoes",
            "Dessert for Dinner",
            "Ceviche (Fish)",
            "Homemade Pizza",
            "Chicken Penne",
            "Beef Tenderloin with Sweet Potato Mash",
            "Baked Fish and Veggies",
            "Dumplings",
            "Slow Cooker Beef and Broccoli",
            "Shrimp Diablo and Rice"]

#All Meals Dictionary
mealDict = {}

#run again validation
def runAgain():
    print("\n")
    againInput = input("Would you like to generate a meal list again? Yes or No: ")
    if againInput == "Yes" or againInput == "Y":
        main()
    else:
        print("Okay. Thanks for letting me help!")

#recipeGenerator function
def recipeGenerator():
    print("\n")
    infoRequest = input("Would you like a recipe? Yes or No: ")
    if infoRequest == "Yes":
        recipeRequest = input("Type the meal name: ")
        if recipeRequest == "Steak Nachos":
            print("\n")
            print("1. Marinate the steak overnight in orange juice, soy sauce, cilantro, Sirarcha, garlic, lime juice, cumin, paprika and Adobo")
            print("2. Cook the steak in sauce pan with the extra marinade.")
            print("3. Chop tomatoes, cucumber, red onion, cilantro and chives.")
            print("4. Layer shredded cheese and tortilla chips with the chopped vegetables and steak.")
            print("5. Enjoy!")
            runAgain()
        elif recipeRequest == "Chicken Meatballs and Tikka Masala":
            print("\n")
            print("1. Marinate ground chicken for fifteen minutes in curry and olive oil. Lime juice is optional.")
            print("2. Mix ground chicken with Panko and roll into balls.")
            print("3. Cook meatballs on a paella at 400 degrees for 25 minutes, turning them halfway.")
            print("3 (cont). At the halfway point, mix in tikka masala sauce, chopped tomatoes, red and white onions.")
            print("4. Enjoy!")
            runAgain()
    else:
        runAgain()

#meal generator function
def mealGenerator():
    numRequest = int(input("How many meals would you like me to select? "))
    #empty List
    randomMeals = []
    print("Here is ", numRequest, "meal(s), randomly selected:")
    randomMeals = random.sample(mealList, numRequest)
    print("\n")
    print(*randomMeals, sep="\n")
    recipeGenerator()
    #runAgain()
    
    #if numRequest < 30:
        #for i in range(numRequest):
            #randomMeals.append(choice(mealList))

#ingredient feature
def ingredientFunction():
    print("Here are your ingredient selections: ")
    print("\n")
    ingredientList = ["Chicken",
                      "Steak",
                      "Pork",
                      "Shrimp",
                      "Fish"]
    print(*ingredientList, sep="\n")
    print("\n")
    ingredientRequest = input("Type one of the following ingredients to receive a list of all meals including that ingredient: ")
    if ingredientRequest == "Chicken":
        sub = "Chicken"
        print("\n")
        print("\n".join([e for e in mealList if sub in e]))
        print("\n")
        runAgain()
    elif ingredientRequest == "Steak":
        sub = "Steak"
        print("\n")
        print("\n".join([e for e in mealList if sub in e]))
        print("\n")
        runAgain()
    elif ingredientRequest == "Pork":
        sub = "Pork"
        print("\n")
        print("\n".join([e for e in mealList if sub in e]))
        print("\n")
        runAgain()
    elif ingredientRequest == "Shrimp":
        sub = "Shrimp"
        print("\n")
        print("\n".join([e for e in mealList if sub in e]))
        print("\n")
        runAgain()
    elif ingredientRequest == "Fish":
        sub = "Fish"
        print("\n")
        print("\n".join([e for e in mealList if sub in e]))
        print("\n")
        runAgain()
    else:
        print("I'm sorry, you seem confused. Let's try again...")
        ingredientFunction()

#type of selection function
def mealType():
    print("\n")
    typeRequest = int(input("Would you like a meal list by (1) Ingredient, (2) Random or (3) All Meals? "))
    if typeRequest == 2:
        mealGenerator()
    elif typeRequest == 1:
        ingredientFunction()
    elif typeRequest == 3:
        print(*mealList, sep="\n")
        recipeGenerator()
    else:
        print("You seem confused...let's start over.")
        mealType()

#main
def main():
    print("\n")
    mealType()

#introduction
print("\n")
print("\n")
print("\n")
print("Looking a little hungry...")
print("I'm Shmooby L. Shmab, you're digital meal planning assistant!")
print("Ready to meal plan for the week? Let me help!")
main()




                 
