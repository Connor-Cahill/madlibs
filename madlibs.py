# Need to find set of 3 stories
#store 3 stories in a list
#create function that gets inputs from user (NEED: Verb, Noun, Adjective, etc.)
#choose random index from list to pick story
##Format the list to inject the user_inputted values into the necessary spots
# make sure user input can only be letters
import random # imported for random.choice()

stories = ["Last summer, my mom and dad took me and {person} on a trip to {location}. The weather there is very {adj}! Northern {location} has many {plural_noun}, and they make {adj2} {plural_noun2} there. Many people also go to {location} to {verb} or see {noun1}. The people that live there love to eat {food} and are very proud of their big {noun2}.",
"Hi! This is {name}, speaking to you from the broadcasting {noun} at the {adj} forum. In case you {verb} in late, the score between the Los Angeles {noun2} and the Boston {noun3} is squeker, 141 to {number}. This has been the most {adj2} game these {noun4} eyes have seen in years. First, one team scores a {noun5}, then the other team comes right back. What an interesting {noun6} to watch!",]


def madlibs():
    random.choice(stories)
    print('Please answer the following to fill in blanks of the mad libs story!')
    if stories[0]:
        person = str(input("Enter a person: "))
        location = str(input('Enter a location: '))
        adj = str(input('Enter in adjective: '))
        plural_noun = str(input('Enter a plural noun: '))
        adj2 = str(input('Enter another adjective: '))
        plural_noun2 = str(input('Enter another plural noun: '))
        verb = str(input('Enter a verb: '))
        noun1 = str(input('Enter a noun: '))
        food = str(input('Enter a food item: '))
        noun2 = str(input('Enter another noun: '))
        return print(stories[0].format(person = person, location = location, adj = adj, plural_noun = plural_noun,
        adj2 = adj2, plural_noun2 = plural_noun2, verb = verb, noun1 = noun1, food = food, noun2 = noun2))
    else:
        name = str(input("Enter a person's name: "))
        noun = str(input('Enter a noun: '))
        adj = str(input('Enter a adjective: '))
        verb = str(input('Enter a verb: '))
        noun2 = str(input('Enter another noun: '))
        noun3 = str(input('Enter another noun: '))
        number = str(input('Enter a number: '))
        adj2 = str(input('Enter another adjective: '))
        noun4 = str(input('Enter another noun: '))
        noun5 = str(input('Enter another noun: '))
        noun6 = str(input('Enter another noun: '))
        return print(stories[1].form(name = name, noun = noun, adj = adj, verb = verb, noun2 = noun2, noun3 = noun3,
        number = number, adj2 = adj2, noun4 = noun4, noun5 = noun5, noun6 = noun6))
madlibs()
