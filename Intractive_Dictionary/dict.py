import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w.capitalize() in data:
        return data[w.capitalize()]
    if w.upper() in data:
        return data[w.upper()]
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(f"Couldn't find the word {w}")
        print(f"Did you mean {get_close_matches(w,data.keys())[0]} instead ? ")
        yn = input(" Enter Y if yes, or N if no:")
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
print()
print()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
print()
print()