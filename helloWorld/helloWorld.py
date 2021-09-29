# Write the code to print a literal string saying "Hello World" (#1)
print("Hello World")
# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function (#2a)
# Sore your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
me = "Cameron"
print("Hello", me)
print("Hello"+me)
# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
# NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
aNum = 42
print("Hello", aNum)
print("Hello"+str(aNum))
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)
food1 = "Soup"
food2 = "Chicharones"
print("I love to eat {} and {}.".format(food1, food2))
print(f"I love to eat {food1} and {food2}.")