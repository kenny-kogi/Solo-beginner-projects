from difflib import get_close_matches
import json
data = json.load(open("data.json"))
input1 = input("Enter the word you want to search for the meaning: ")

def read(word):

        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif len(get_close_matches(word,data.keys())) > 0:
            ans = input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead.\nTo continue type (Yes/No:) ")
            if ans.lower() == "yes":
                return data[get_close_matches(word,data.keys())[0]]
            elif ans.lower() == "no":
                return "Thank you."
            elif word.upper() in data:
                return data[word.upper()]
            else:
                return "Wrong entry!!! "
        else:
            return "That word does not exists please re check "

kenny = read(input1.lower())
if type(kenny) == list:
    for item in kenny:
        print(item)

else:
    print(read(input1.lower()))
