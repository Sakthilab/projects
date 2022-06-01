programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
     "Function": "A piece of code that you can easily call over and over again."
}

#Adding new key pair value to the existing dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# create an empty dictionary

empty_dictionary = {}

#wipe an existing dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
