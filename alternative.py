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

#The counter is to allow us to alternate the case odd and even numbers 
counter = 0

for word in user_string_split:
    
    # If even, the upper case version of the word in the current iteration of the loop will be added to our blank list, and lower case for an odd number
    if counter % 2 == 0:
        alternating_word_string.append(word.upper())
    else:
        alternating_word_string.append(word.lower())
    counter += 1

# The list is then converted back into a string with a space in between each word/item
final_string = " ".join(alternating_word_string)
print(final_string)

# I appreciate there is probably a way of doing this without the counter on part two, making it even neater
# However I couldn't figure out how to find the index number of "word" in each iteration of the "for" loop in order to divide it by 2
# If that is simple enough to explain in the feedback, I would love to know, thank you!