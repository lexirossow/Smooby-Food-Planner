#What's for dinner?
#Smooby L. Smab, the digital meal planning assitant

import random
from random import choice, sample
random.seed(4)

#All Meals List
mealList = ["Ocean Snot", "Boogers", "Luna", "Bush Meat", "Rotten Apples"]

#All Meals Dictionary
mealDict = {"Ocean Snot": "Recipe1"}

#run again validation
def runAgain():
    print("\n")
    againInput = input("Would you like to generate a meal list again? Yes or No: ")
    if againInput == "Yes":
        main()
    else:
        print("Okay. Thanks for letting me help!")

#recipeGenerator function
def recipeGenerator():
    print("\n")
    infoRequest = input("Would you like a recipe? Yes or No: ")
    if infoRequest == "Yes":
        recipeRequest = input("Type the meal name: ")
        if recipeRequest == key.mealDict():
            print(value)
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
    #recipeGenerator()
    runAgain()
    
    #if numRequest < 30:
        #for i in range(numRequest):
            #randomMeals.append(choice(mealList))

#main
def main():
    print("\n")
    mealGenerator()

#introduction
print("\n")
print("\n")
print("\n")
print("Looking a little hungry, Lexstophe...")
print("I'm Shmooby L. Shmab, you're digital meal planning assistant!")
print("Ready to meal plan for the week? Let me help!")
main()






                 
