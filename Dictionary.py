import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#Input function
def input_function():
    word = input("Enter the word you want to search for: ")
    return word


#Word meaning Finder Logic
def translate(word):
    if word.lower() in data.keys():
        return data[word.lower()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    else:
        return(possible_nearest(word.lower()))




def possible_nearest(word):
    closest_word = get_close_matches(word , data.keys())
    if (len(closest_word) > 0):
            choice  = input("Did you mean " + closest_word[0] +" instead?" + "\nEnter Y or N: ")
            if choice == "Y":
                return data[closest_word[0]]
            elif choice == "N":
                return("No Such Word found. Try again!!")
    else:
        return ("No such word. Try again!!")



while(1):
    print(translate(input_function()))
