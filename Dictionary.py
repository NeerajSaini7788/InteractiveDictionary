import json
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
        return("Enable to find word")


while(1):
    print(translate(input_function()))
