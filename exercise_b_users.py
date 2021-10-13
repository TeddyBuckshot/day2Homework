users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the array of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an array of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "Fluffy"
# 10. Add another person to the users dictionary

print("\n")
print("Jonathans twitter is: ", users["Jonathan"]["twitter"])                     # prints Jonathans twitter handle

print("Erik's hometown is: ", users["Erik"]["home_town"])                         # prints Erik's hometown

print("Erik's Lotto numbers are: ", users["Erik"]["lottery_numbers"])             # prints Eriks Lottery numbers

avrilPet = users["Avril"]["pets"][0]["species"]             # stores the species of avrilsPet in a new variable
print("Avrils pet is a: ", avrilPet, "\n")                  # and prints it

erikLottoList = users["Erik"]["lottery_numbers"]                                # initialises new List containing Eriks lottery no's.
print("Lowest number in Erik's numbers is: ", min(erikLottoList), "\n")         # and prints the lowest number.

avrilLottoList = users["Avril"]["lottery_numbers"]          # initialises new List containing Avrils lottery no's.
avrilEven = []                                              # initialises empty List 
for num in avrilLottoList:                                  
    if num % 2 == 0:                                        # for all the items in avrils lottery numbers, IF they divide by 2 with no remainder --
        avrilEven.append(num)                               # They are EVEN. if they are EVEN they are added to the empty List from before.
print("Avrils EVEN lotto numbers: ", avrilEven, '\n')       # new List is then printed

erikLottoList.append(7)                                                         # add no. 7 to Eriks numbers.
print("Erik has added a number: ", erikLottoList, "\n")

erikHome = users["Erik"]["hometown"] = "Edinburgh"                              # new variable = Eriks hometown, which is also being reset to 'Edinburgh'
print("Erik's new hometown is: ", erikHome, "\n")                               # new variable then printed

erikPet = users["Erik"]["pets"]                                                 # new List containing Erik's pets
erikPet.append({"name":"Fluffy", "species":"dog"})                              # adding new pet to dictionary within a list within a dictionary within a list within.........
print("Erik's pets with newly added DOG: ", erikPet, "\n")                      # Print List of pets to show newly added Dog.

users["Sam"] = {"twitter":"samS", "lottery_numbers":[1,2,3,4,5,6,7], "home_town":"Linlithgow", "pets":[{"name":"leia", "species":"dog"}]}
for key, value in users.items() :
  if key == "Sam":                                                              # new user added above here, all in one line. could be more elegant!
    print ("New user added: ", key, value)                                      # loop with conditional used to select the new user by KEY then display all values within.




