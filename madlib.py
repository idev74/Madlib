
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

print("Hello there! Time for a mad lib... ")
name = input("First, what is your name? ")
print(f"Hi, {name}!")

celeb = input("Name a celebrity: ")

animal = input("Name an animal: ")
animal = str.lower(animal)

verb1 = input("Verb: ")
verb1 = str.lower(verb1)

adverb = input("Adverb: ")
adverb = str.lower(adverb)

noun = input("Noun: ")
noun = str.lower(noun)

color = input("Color or Pattern: ")
color = str.lower(color)

place = input("Place: ")

drink = input("Drink name: ")
drink = str.lower(drink)

adj = input("Adjective: ")
adj = str.lower(adj)

verb2 = input("Verb ending in -ed: ")
verb2 = str.lower(verb2)

print(f"On a cloudy fall day, {celeb}'s pet {animal} decided to {verb1} {adverb}.\nAfter they were done, the {animal} grabbed their favorite {color} {noun} and walked down the block.\nFeeling parched, they went to {place} and ordered a(n) {drink}.\nAt the end of a long and {adj} day, the little {animal} {verb2} up to {celeb} and lulled to sleep.")



































# --------------------------------------------------
# Partial solution
























# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")