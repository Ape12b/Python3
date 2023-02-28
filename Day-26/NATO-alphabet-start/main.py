# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

dict_NATO = {value.letter: value.code for (index, value) in student_data_frame.iterrows()}
# TODO 1. Create a dictionary in this format:
print(dict_NATO)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter the name: ")
user_phoenetic_name = {letter: dict_NATO[letter.upper()] for letter in user_name}
print(user_phoenetic_name)
