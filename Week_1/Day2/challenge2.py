# First, the user enter a word
user_word = input("Enter a word :")   # Ask the user to input a word and store it in the variable `user_word`


def mapper_letters_to_index(word):
    # Initialize an empty dictionary to store the results
    mapping = {}    # This dictionary will map each letter to a list of its indices in the word

    # Iterate over each character in the word along with its index
    for index, lettre in enumerate(word):
         # If the letter is already a key in the dictionary, append the index to its list 
        if lettre in mapping:
            mapping[lettre].append(index)
        else:
             # Otherwise, create a new entry in the dictionary with a list containing the current index 
            mapping[lettre] = [index]

    return mapping     # Return the completed dictionary mapping letters to their indices

#Call the function and display the result
result = mapper_letters_to_index(user_word)   # Pass the user's word to the function and store the result
print(result)


##############################################################################################################################
#Here’s the Approach I Used
#  implemented a dictionary-based solution to map each letter of a word to its corresponding indices.
#  Here’s how it works step by step:

# 1st : Ask the user for a word:
#The program starts by prompting the user to enter a word.

# 2nd Define the mapper_letters_to_index function:
# This function takes the word as input and processes it to create the mapping.
# The process begin by :
                      #Initialize an empty dictionary:
                      #A dictionary is created to store letters as keys and their indices as values.

                      # Iterate through the word with enumerate:
                      # Each letter in the word is iterated over along with its index using enumerate.

                      # Update the dictionary:

                      # If the letter already exists in the dictionary, the index is appended to its list of indices.
                      # Otherwise, a new entry is created with the letter as the key and a list containing the index as the value.

# Finaly, we display the result:
# The final dictionary, mapping each letter to its indices, is printed.