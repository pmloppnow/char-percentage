# This program determines how many times a character was used in a string and returns a percentage.

# Function Definition
def percent(character,string):
    global count
    for char in string:
        if char == character:
            count += 1
    return int(count / len(string) * 100)
    
# Variables
string = input("Enter a string of characters: ")
while len(string) == 0:
    string = input("You may not submit an empty string. Enter a string of characters: ")
character = input("Enter a single character: ")
while len(character) != 1:
    character = input("Enter a single character: ")
count = 0
x = percent(character, string)
denominator = len(string)

# Output
print(f"The character '{character}' accounts for {count}/{denominator} or roughly {x}% of the total characters in '{string}'.")