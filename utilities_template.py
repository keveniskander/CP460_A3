"""
-----------------------------
CP460 (Fall 2020)
Utilities
Assignment 3
-----------------------------
"""

# Functions:
# 1- get_base(base_type)
# 2- file_to_text(filename)
# 3- text_to_file(text,filename)
# 4- text_to_block(text,b_size,padding=0,pad=PAD)
# 5- def get_positions(text,base)
# 6- def clean_text(text,base)
# 7- def insert_positions(text, positions)
# 8- def shift_string(s,n,d='l')
# 9- def new_matrix(r,c,fill)
# 10-def print_matrix(matrix)
# 11-def is_plaintext(text, dict_list, threshold=0.9)
# 12-def analyze_text(text, dict_list)
# 13-def text_to_words(text)
# 14-def load_dictionary(dict_file)
# 15-def get_language_freq(language='English')
 
import string
import math

DICT_FILE = 'engmix.txt'
PAD = 'q'
BLOCK_MAX_SIZE = 20

"""
----------------------------------------------------
Parameters:   None 
Return:       freq (list of floats) 
Description:  Return frequencies of characters in a given language
              Default language is English
---------------------------------------------------
"""
def get_language_freq(language='English'):
    if language == 'English':
        return [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    else:
        print('Error(get_language_freq): Unsupported language')
        return []
