user_string = input("Please enter sentence: ")

#Part one: Alternating Letters

# This empty string will contain the altered upper/lower letters
new_user_string = ""

for i in range(len(user_string)):

    # Checks if the index of each letter in the string is even or not
    # If even, an upper case version of that letter is added to the new string.  If odd, a lower case letter is added
    if i  % 2 == 0:
        new_user_string += user_string[i].upper()
    else:
        new_user_string += user_string[i].lower()

print(new_user_string)


#Part two: Alternating words

user_string_split = user_string.split()

# This time we're using a list instead of a string to contain the altered case words
alternating_word_string = []

for word in user_string_split:
    
    # If even, the upper case version of the word in the current iteration of the loop will be added to our blank list
    if user_string_split.index(word) % 2 == 0:
        alternating_word_string.append(word.upper())
    else:
        alternating_word_string.append(word.lower())
    

# The list is then converted back into a string with a space in between each word/item
final_string = " ".join(alternating_word_string)
print(final_string)

