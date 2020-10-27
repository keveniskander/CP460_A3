"""
-----------------------------
CP460 (Fall 2020)
Name: Keven Iskander
ID:   160634540
Assignment 3
-----------------------------
"""

MAX_KEY_L = 17
CIPHER_SHIFT_FACTOR = 180


"""
----------------------------------------------------
            Task 1: Utilities
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   text1 (str)
              text2 (str)
Return:       matches (int)
Description:  Compares two strings and returns number of matches
Assert:       text1 and text2 are strings
----------------------------------------------------
"""
def compare_texts(text1,text2):
    
    assert type(text1) == str
    assert type(text2) == str

    matches = 0
    if len(text1)<len(text2):
        for i in range(len(text1)):
            if text1[i] == text2[i]:
                matches += 1
    else:
        for j in range(len(text2)):
            if text2[j] == text1[j]:
                matches +=1
    return matches

"""
----------------------------------------------------
Parameters:   text (str)
              [optional] base: str
Return:       count_list (list of floats) 
Description:  Finds character frequencies (count) in a given text
              Default is English language (counts both upper and lower case)
              Otherwise returns frequencies of characters defined in base
Assert:       text is a string
----------------------------------------------------
"""
def get_freq(text,base = None):
    # your solution here
    return count_list

"""
----------------------------------------------------
Parameters:   text(str)
              [optional] base_type(str)
Return:       I (float): Index of Coincidence
Description:  Computes and returns the index of coincidence 
              Uses English alphabets, or specified base_type
Asserts:      text is a string
----------------------------------------------------
"""
def index_of_coin(text,base_type = None):
    # your solution here
    return I

"""
----------------------------------------------------
Parameters:   text (str)
              [optional] language (str)
Return:       result (float)
Description:  Calculates the Chi-squared statistics 
              for given text against given language
              Only alpha characters are considered
Asserts:      text is a string
Errors:        if language is unsupported:
                    print error msg: 'Error(chi_squared): unsupported language'
                    return -1
----------------------------------------------------
"""
def chi_squared(text,language='English'):
    # your solution here
    return result

"""
----------------------------------------------------
            Task 2: Vigenere Cipher
----------------------------------------------------
"""
"""
----------------------------------------------------
Parameters:   None 
Return:       v_square (list of strings)
Description:  Constructs Vigenere square as list of strings
              element 1 = "abcde...xyz"
              element 2 = "bcde...xyza" (1 shift to left)
              ...
----------------------------------------------------
"""
def _vigenere_square():
    # your solution here
    return v_square

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (str)
Return:       ciphertext (str)
Description:  Encryption using Vigenere Cipher
              Key could be an autokey or a running key
Asserts:      plaintext is a string
Error:        if invalid key:
                print error msg: Error(e_vigenere): invalid key
                return empty string
----------------------------------------------------
"""
def e_vigenere(plaintext,key):
    # your solution here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (str)
Return:       plaintext (str)
Description:  Decryption using Vigenere Cipher
              Key could be an autokey or a running key
Asserts:      ciphertext is a string
Error:        if invalid key:
                print error msg: Error(e_vigenere): invalid key
                return empty string
----------------------------------------------------
"""
def d_vigenere(ciphertext,key):
    # your solution here
    return plaintext


"""
----------------------------------------------------
            Task 3: Shift Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   plaintext (str)
              key (int,str): (shifts,base)
Return:       ciphertext (str)
Description:  Encryption using shift cipher
              The base is applied to circular left shift by "shifts"
              if shifts is None, The shift is done on lower case alphabet
                  case of the characters is preserved.
Asserts:      plaintext is a string
Error:        if invalid key:
                print error msg: Error(e_shift): invalid key
                return empty string
----------------------------------------------------
"""
def e_shift(plaintext,key):
    # your solution here
    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              key (int,str): (shifts,base)
Return:       plaintext (str)
Description:  Decryption using shift cipher
              The base is applied to circular left shift by "shifts"
              if shifts is None, The shift is done on lower case alphabet
                  case of the characters is preserved.
Asserts:      ciphertext is a string
Error:        if invalid key:
                print error msg: Error(d_shift): invalid key
                return empty string
----------------------------------------------------
"""
def d_shift(ciphertext,key):
    # your solution here
    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              [optional] base_type (str/None)
Return:       key (int)
              plaintext (str)
Description:  Uses chi_squared method to restore plaintext
              Assume 
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cryptanalysis_shift(ciphertext,base_type = None):
    # your solution here
    return key,plaintext

"""
----------------------------------------------------
            Task 4: Vigenere Cryptanalysis
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   blocks (list of str)
Return:       baskets: (list of str)
Description:  Create k baskets, where k = key length = block size
              basket[i] contains character ith from each block in consecutive order
              Assume all blocks are of the same type
----------------------------------------------------
"""
def _blocks_to_baskets(blocks):
    # your solution here
    return baskets

"""
----------------------------------------------------
Parameters:   ciphertext(str)
Return:       list of two key lengths [int,int]
Description:  Uses Friedman's test to compute key length
              returns best two candidates for key length
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def friedman(ciphertext):
    # your solution here
    return [k1,k2]

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              [optional] max_key_length (int)
Return:       list of two key lengths [int,int]
Description:  Uses Cipher shifting to compute key length
              returns betw two candidates for key length
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cipher_shifting(ciphertext,max_key = MAX_KEY_L):
    # your code here
    return [k1,k2]

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       list of two key lengths
Description:  Combines results of Friedman and Cipher shifting
              to produce a list of best candidates
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def _cryptanalysis_vigenere_key_length(ciphertext):
    # your code here
    return [k1,k2]

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       key (str)
              plaintext (str)
Description:  Cryptanalysis of Vigenere cipher
              If cryptanalysis fails, return two empty strings
Asserts:      ciphertext is a non-empty string
----------------------------------------------------
"""
def cryptanalysis_vigenere(ciphertext):
    # your code here
    return key,plaintext

"""----------------------------
Columnar Transposition Cipher
----------------------------"""