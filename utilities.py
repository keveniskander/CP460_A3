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
Parameters:   base_type (str) 
Return:       result (str)
Description:  Return a base string containing a subset of ASCII charactes
              Defined base types:
              lower: lower case characters
              upper: upper case characters
              alpha: upper and lower case characters
              num: numerical characters
              lowernum: lower case and numerical characters
              uppernum: upper case and numerical characters
              alphanum: upper, lower and numerical characters
              nonalpha: all non alphabetical characters
              special: punctuations and special characters (no white space)
              all: upper, lower, numerical and special characters
---------------------------------------------------
"""
def get_base(base_type):
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
            
    result = ''
    if base_type == 'lower':
        result = lower
    elif base_type == 'upper':
        result = upper
    elif base_type == 'alpha':
        result = upper + lower
    elif base_type == 'num':
        result = num
    elif base_type == 'lowernum':
        result = lower + num
    elif base_type == 'uppernum':
        result = upper + num
    elif base_type == 'alphanum':
        result = upper + lower + num
    elif base_type == 'special':
        result = special
    elif base_type == 'nonalpha':
        result = special + num
    elif base_type == 'all':
        result = upper + lower + num + special
    else:
        print('Error(get_base): undefined base type')
        result = ''
    return result


"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""
def file_to_text(filename):
    # put your code here
    infile = open(filename,'r')
    contents = infile.read()
    infile.close()
    return contents

"""
----------------------------------------------------
Parameters:   text (str)
              filename (str)            
Return:       no returns
Description:  Utility function to write any given text to a file
              If file already exist, previous content will be erased
---------------------------------------------------
"""
def text_to_file(text, filename):
    # put your code here
    outfile = open(filename,'w')
    outfile.write(text)
    outfile.close()
    return

"""
----------------------------------------------------
Parameters:   text (str)
              block_size (int)
              padding (bool): False/default = no padding, True = padding
              pad (str): default = PAD
Return:       blocks (list)
Description:  Create a list containing strings each of given block size
              if padding flag is set, pad using given padding character
              if no padding character given, use global PAD
Asserts:      text is a string and b_size is a positive integer
---------------------------------------------------
"""
def text_to_blocks(text,b_size,padding = 0,pad =PAD):
    
    assert type(text) == str
    assert type(b_size) == int
    assert b_size > 0

    blocks = []
    i = 0
    
    while i < (len(text)):
        if len(text) - i < b_size and padding == 1:
           
            blocks.append(text[i:i+b_size] + (pad * (b_size-(len(text)-i))))
                
        else:
            blocks.append(text[i:i+b_size])
        i+=b_size
    return blocks

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       positions (2D list)
Description:  Analyzes a given text for any occurrence of base characters
              Returns a 2D list with characters and their respective positions
              format: [[char1,pos1], [char2,pos2],...]
              Example: get_positions('I have 3 cents.','c.h') -->
              [['h',2],['c',9],['.',14]]
              Text and base are not changed
Asserts:      text and base are strings
---------------------------------------------------
"""
def get_positions(text,base):
    
    assert type(text) == str
    assert type(base) == str

    positions = []

    for i in range(len(text)):
        for j in range(len(base)):
            if text[i] == base[j]:
                positions.append([base[j], i])

    return positions

"""
----------------------------------------------------
Parameters:   text (str)
              base (str)
Return:       updated_text (str)
Description:  Removes all base characters from text
Asserts:      text and base are strings
---------------------------------------------------
"""
def clean_text(text,base):
    
    assert type(text) == str
    assert type(base) == str

    updated_text = text

    for i in range(len(text)):
        for j in range(len(base)):
            if text[i] == base[j]:
                
                updated_text = updated_text.replace(base[j], '')


    return updated_text

"""
----------------------------------------------------
Parameters:   text (str)
              positions (lsit): [[char1,pos1],[char2,pos2],...]]
Return:       updated_text (str)
Description:  Inserts all characters in the positions 2D list into their respective
Asserts:      text is a string and positions is a list
---------------------------------------------------
"""
def insert_positions(text, positions):
    
    assert type(text) == str
    assert type(positions) == list

    updated_text = text

    for i in range(len(positions)):
        updated_text = updated_text[:positions[i][1]] + positions[i][0] + updated_text[positions[i][1]:]
    return updated_text

"""
----------------------------------------------------
Parameters:   text (string): input string
              shifts (int): number of shifts
              direction (str): 'l' or 'r'
Return:       update_text (str)
Description:  Shift a given string by given number of shifts (circular shift)
              If shifts is a negative value, direction is changed
              If no direction is given or if it is not 'l' or 'r' set to 'l'
Asserts:      text is a string and shifts is an integer
---------------------------------------------------
"""
def shift_string(text,shifts,direction='l'):
    
    assert type(text) == str
    assert type(shifts) == int

    updated_text = text
    accepted_directions = 'rRlL'

    if direction not in accepted_directions:
        direction = 'l'

    if abs(shifts) > len(text):

        if shifts > 0:
            shifts = shifts % len(text)
        else:
            shifts = abs(shifts) % len(text)
            shifts = -shifts

    if shifts > 0:

        if direction == 'r' or direction == 'R':
            
            updated_text = updated_text[-shifts:] + updated_text[:-shifts]
            # print('r1')
        if direction == 'l' or direction == 'L':
        
            updated_text = updated_text[shifts:] + updated_text[:shifts]
            # print('l1')

    elif shifts < 0:
        if direction == 'r' or direction == 'R':
            
            updated_text = updated_text[-shifts:] + updated_text[:-shifts]
            # print('r2')
        if direction == 'l' or direction == 'L':
            
            updated_text = updated_text[shifts:] + updated_text[:shifts]
            # print('l2')

    return updated_text

"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""
def new_matrix(r,c,fill):
    # put your code here
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[fill] * c for i in range(r)]

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
                items separated by a tab
#               Assumes given parameter is a valid matrix
---------------------------------------------------
"""
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return

"""
----------------------------------------------------
Parameters:   text (str)
              dict_list (str): dictionary list
              threshold (float): number between 0 to 1
Return:       True/False
Description:  Check if a given file is a plaintext
              If #matches/#words >= threshold --> True
                  otherwise --> False
              If invalid threshold or not given, default is 0.9
              An empty string should return False
              Assumes a valid dict_list is passed
---------------------------------------------------
"""
def is_plaintext(text, dict_list, threshold=0.9):
    if text == '':
        return False
    result = analyze_text(text, dict_list)
    percentage = result[0]/(result[0]+result[1])
    if threshold <= 0 or threshold > 1:
        threshold = 0.9
    if percentage >= threshold:
        return True
    return False

"""
----------------------------------------------------
Parameters:   text (str)
              dict_list (list)
Return:       match (int)
              mismatch (int)
Description:  Reads a given text, checks if each word appears in given dictionary
              Returns number of matches and number of mismatches.
              Words are compared in lowercase
              Assumes a proper dict_list
Asserts:      text is a string and dict_list is a string
---------------------------------------------------
"""
def analyze_text(text, dict_list):
    assert type(text) == str and type(dict_list) == list, 'invalid inputs'
    word_list = text_to_words(text)
    alphabet = get_base('lower')
    match = 0
    mismatch = 0
    for w in word_list:
        if w.isalpha():
            list_num = alphabet.index(w[0].lower())
            if w.lower() in dict_list[list_num]:
                match+=1
            else:
                mismatch+=1
        else:
            mismatch+=1
    return match,mismatch

"""
----------------------------------------------------
Parameters:   text (str)
Return:       word_list (list)
Description:  Reads a given text
              Returns a list of strings, each pertaining to a word in file
              Words are separated by a white space (space, tab or newline)
              Gets rid of all special characters at the start and at the end
Asserts:      text is a string
---------------------------------------------------
"""
def text_to_words(text):

    assert type(text) == str, 'invalid text'

    special_char = get_base('special')
    word_list = text.split()
    for a in range(len(word_list)):

        if len(word_list[a])>1:
            word_list[a] = word_list[a].rstrip(special_char)
            word_list[a] = word_list[a].lstrip(special_char)

        if word_list[a] == '':
            word_list[a] = ' '

    return word_list

"""
----------------------------------------------------
Parameters:   dict_file (str): filename
Return:       dict_list (list): 2D list
Description:  Reads a given dictionary file
              dictionary is assumed to be formatted: each word in a separate line
              Returns a list of lists, list 0 contains all words starting with 'a'
              list 1 all words starting with 'b' and so forth.
Asserts:      dict_file is a non-empty string
---------------------------------------------------
"""
def load_dictionary(dict_file):

    assert type(dict_file) == str, 'invalid dict_file'
    assert len(dict_file) > 0, 'invalid dict_file'

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dict_list = [[] for i in range(len(alpha))]

    # print(dict_list)
    file1 = open(dict_file, encoding="ISO-8859-15")
    # a = len(alpha) 
    line = file1.readline() 

    while line:

        line = line.strip()
        b = alpha.find(line[0])
        dict_list[b].append(line)

        line = file1.readline()
        

    return dict_list

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
