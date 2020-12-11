import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Create DataFrame from CSV
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
"""
   letter      code
0       A      Alfa
1       B     Bravo
2       C   Charlie
"""

# This doesn't give the format we require:
# df_dict = df.to_dict()
# print(df_dict)
"""{'letter': {0: 'A', 1: 'B', 2: 'C', ... }, 'code': {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', ... }"""

# Create dictionary in the correct format
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)
"""
{'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', ...}
"""


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Type a word : ").upper()
"""John"""
code_list = [nato_dict[letter] for letter in word]
print(code_list)
"""['Juliet', 'Oscar', 'Hotel', 'November']"""
