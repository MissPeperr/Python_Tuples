'''
    1. Create a tuple named zoo that contains 10 of your favorite animals.
'''
zoo = ("Red Panda", "Pig", "Tortise", "Bear", "Elephant", "Giraffe", "Rhino","Condor", "Lemur", "Kangaroo")

'''
    2. Find one of your animals using the tuple.index(value) syntax on the tuple.
'''
print(f'The Red Pand is at index {zoo.index("Red Panda")}')

'''
    3. Determine if an animal is in your tuple by using value in tuple syntax
'''
animal_to_find = "Pig"
if animal_to_find in zoo:
    print(f'The animal {animal_to_find} was found')

'''
    4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax:
        children = ("Sally", "Hansel", "Gretel", "Svetlana")
        (first_child, second_child, third_child, fourth_child) = children
        print(first_child) # Output is "Sally"
        print(second_child) # Output is "Hansel"
        print(third_child) # Output is "Gretel"
        print(fourth_child) # Output is "Svetlana"
    Create a variable for the animals in your zoo tuple, and print them to the console.
'''
(most_favorite, pig, tortise, bear, elephant, giraffe, least_favorite, condor, lemur, roo) = zoo
print("ALL ZOO ANIMALS:")
for animal in zoo:
    print(animal)

'''
    5. Convert your tuple into a list.
'''
zoo = list(zoo)
print(f'zoo tuple is now a list: {zoo}')

'''
    6. Use extend() to add three more animals to your zoo.
'''
zoo.extend(["Aardvark", "Squirrel", "Lion"])
print(f'Zoo has been extended: {zoo}')

'''
    7. Convert the list back into a tuple.
'''
zoo = tuple(zoo)
print(f'zoo list is now a tuple: {zoo}')
