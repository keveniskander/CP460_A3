"""
-----------------------------
CP460 (Fall 2020)
Name: Keven Iskander
ID:   160634540
Assignment 3
-----------------------------
"""

import utilities
import math

MAX_KEY_L = 17
CIPHER_SHIFT_FACTOR = 26


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
    
    assert type(text) == str
    
    if base == None:

        alpha = utilities.get_base('lower')
        count_list = [0] * len(alpha)

        for i in range(len(text)):
            for j in range(len(alpha)):
                if text[i].upper() == alpha[j] or text[i].lower() == alpha[j]:
                    count_list[j] += 1

    else:

        alpha = utilities.get_base(base)
        count_list = [0] * len(alpha)

        for i in range(len(text)):
            for j in range(len(alpha)):
                if text[i] == alpha[j]:
                    count_list[j] += 1

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
    
    assert type(text) == str

    if len(text) == 0:
        return 0.0

    I = 0.0
    freq = get_freq(text, base_type)
    freq_sum = sum(freq)
    if freq_sum == 0:
        return 0.0
    it_freq_sum = 0.0

    for i in range(len(freq)):
        it_freq_sum += (freq[i]*(freq[i]-1))
    I = 1/(freq_sum*(freq_sum-1))
    I *= it_freq_sum

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
    
    assert type(text) == str

    result = 0.0
    get_lang_freq = utilities.get_language_freq(language)
    get_text_freq = get_freq(text, base=None)
    # print(get_text_freq)

    if get_lang_freq == []:
        print('Error(chi_squared): unsupported language')
        return -1

    if len(text) == 0:
        return -1

    for i in range(len(get_text_freq)):
        Ci = get_text_freq[i]
        Ei = get_lang_freq[i] * sum(get_text_freq)
        result += ((Ci-Ei)**2)/Ei
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
    
    v_square = []
    c_element = utilities.get_base('lower')
    i = 0
    while i < len(c_element):
        v_square.append(c_element)
        c_element = utilities.shift_string(c_element,1,direction='l')
        i += 1

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
def _e_viginere_auto(plaintext,key):

    ciphertext = ''
    cipherstring = plaintext
    key_string = cipherstring
    specials = utilities.get_base('nonalpha')
    
    positions = utilities.get_positions(cipherstring, ' ' + specials + '\n')
    cipherstring = utilities.clean_text(cipherstring, ' ' + specials + '\n') 
    key_string = utilities.clean_text(key_string, ' ' + specials + '\n')
    key_string = key + key_string[0:]

    # print(cipherstring)
    # print(key_string)

    v_square = _vigenere_square()
    lower = utilities.get_base('lower')

    for i in range(len(cipherstring)):
        ri = v_square[0].find(cipherstring[i].lower())
        ci = lower.find(key_string[i].lower())
        # print(ri,ci)
        # print(v_square[ci][ri])
        if cipherstring[i].islower()==True:
            ciphertext = ciphertext + v_square[ci][ri]
        else:
            ciphertext = ciphertext + v_square[ci][ri].upper()
    # ciphertext = utilities.insert_positions(ciphertext, positions)

    ciphertext = utilities.insert_positions(ciphertext, positions)

    return ciphertext

def _e_viginere_run(plaintext,key):
    
    ciphertext = ''
    cipherstring = plaintext
    key_string = ''
    specials = utilities.get_base('nonalpha')
    count = 0
    i = 0

    positions = utilities.get_positions(cipherstring, ' ' + specials + '\n')
    cipherstring = utilities.clean_text(cipherstring, ' ' + specials + '\n')

    while i < len(cipherstring):
        key_string = key_string + key[count]
        count+=1
        if count == len(key):
            count = 0
        i += 1

    # print(cipherstring, len(cipherstring))
    # print(key_string, len(key_string))

    v_square = _vigenere_square()
    lower = utilities.get_base('lower')

    for j in range(len(cipherstring)):
        ri = v_square[0].find(cipherstring[j].lower())
        ci = lower.find(key_string[j].lower())

        if cipherstring[j].islower()==True:
            ciphertext = ciphertext + v_square[ci][ri]
        else:
            ciphertext = ciphertext + v_square[ci][ri].upper()

    ciphertext = utilities.insert_positions(ciphertext, positions)

    return ciphertext


def e_vigenere(plaintext,key):

    assert type(plaintext) == str

    ciphertext = plaintext
    if len(key) == 1:
        ciphertext = _e_viginere_auto(ciphertext, key)
    elif len(key) == 0:
        print('Error(e_vigenere): invalid key')
        return ''
    else:
        ciphertext = _e_viginere_run(ciphertext, key)
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

def _d_viginere_auto(ciphertext,key):

    plaintext = ''
    plainstring = ciphertext
    key_string =  key
    specials = utilities.get_base('nonalpha')

    positions = utilities.get_positions(plainstring, ' ' + specials + '\n')
    plainstring = utilities.clean_text(plainstring, ' ' + specials + '\n')
    ciphertext = utilities.clean_text(ciphertext, ' ' + specials + '\n')

    v_square = _vigenere_square()
    lower = utilities.get_base('lower')

    # print(plainstring)
    # print(key_string)

    for i in range(len(plainstring)):
        ci = lower.find(key_string[i].lower())
        ri = v_square[ci].find(ciphertext[i].lower())
        # print(ciphertext[i].lower())
        # print(ci, ri)
        if plainstring[i].islower()==True:
            plaintext = plaintext + v_square[0][ri]
            key_string = key_string + v_square[0][ri]
        else:
            plaintext = plaintext + v_square[0][ri].upper()
            key_string = key_string + v_square[0][ri].upper()
        # print(plaintext)

    plaintext = utilities.insert_positions(plaintext, positions)

    return plaintext

def _d_viginere_run(ciphertext,key):
    
    plaintext = ''
    plainstring = ciphertext
    key_string = ''
    specials = utilities.get_base('nonalpha')
    count = 0
    i = 0

    positions = utilities.get_positions(plainstring, ' ' + specials + '\n')
    plainstring = utilities.clean_text(plainstring, ' ' + specials + '\n')
    ciphertext = utilities.clean_text(ciphertext, ' ' + specials + '\n')

    while i < len(plainstring):
        key_string = key_string + key[count]
        count+=1
        if count == len(key):
            count = 0
        i += 1

    v_square = _vigenere_square()
    lower = utilities.get_base('lower')

    for j in range(len(plainstring)):
        ci = lower.find(key_string[j].lower())
        ri = v_square[ci].find(ciphertext[j].lower())

        if plainstring[j].islower()==True:
            plaintext = plaintext + v_square[0][ri]
        else:
            plaintext = plaintext + v_square[0][ri].upper()

    plaintext = utilities.insert_positions(plaintext, positions)

    return plaintext

def d_vigenere(ciphertext,key):
    
    assert type(ciphertext) == str
    
    if len(key) == 1:
        plaintext  = _d_viginere_auto(ciphertext, key)
    elif len(key) == 0:
        print('Error(d_vigenere): invalid key')
        return ''
    else:
        plaintext = _d_viginere_run(ciphertext, key)
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
    
    assert type(plaintext) == str

    ciphertext = ''

    if type(key) != tuple or type(key[0]) != int or  (type(key[1]) == str and len(key[1])<1) or (key[1]!=None and type(key[1]) != str):
        print('Error(e_shift): invalid key')   
        return ''

    if key[1]==None:
        base = utilities.get_base('lower')
    elif len(key[1]) != 0:
        base = key[1]
    else:
        print('Error(e_shift): invalid key')   
        return ''

    shifts = key[0]

    for i in range(len(plaintext)):
        if key[1] == None and plaintext[i].isupper():
            j = base.find(plaintext[i].lower())
        else:
            j = base.find(plaintext[i])
        if j!= -1:
            shifted = utilities.shift_string(base, shifts)
            if key[1] == None and plaintext[i].isupper():
                ciphertext = ciphertext + shifted[j].upper()
            else:
                ciphertext = ciphertext + shifted[j]
        else:
            ciphertext = ciphertext + plaintext[i]

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
    
    assert type(ciphertext) == str

    if type(key) != tuple or type(key[0]) != int or (type(key[1]) == str and len(key[1])<1) or (key[1]!=None and type(key[1]) != str):
        print('Error(d_shift): invalid key')   
        return ''

    plaintext = ''

    if key[1] == None:
        base = utilities.get_base('lower')
    elif len(key[1])!=0:
        base = key[1]
    else:
        print('Error(d_shift): invalid key')
        return ''

    shifts = key[0]

    for i in range(len(ciphertext)):
        if key[1] == None and ciphertext[i].isupper():
            j = base.find(ciphertext[i].lower())
        else:
            j = base.find(ciphertext[i])
        if j != -1:
            shifted = utilities.shift_string(base, shifts, direction='r')
            if key[1] == None and ciphertext[i].isupper():
                plaintext = plaintext + shifted[j].upper()
            else:
                plaintext = plaintext + shifted[j]
        else:
            plaintext = plaintext + ciphertext[i]

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
    assert type(ciphertext) == str
    # assert len(ciphertext)!=0

    if base_type == None:
        base = utilities.get_base('lower')
    else:
        base = utilities.get_base(base_type)

    key_array = []
    plaintext_array = []
    chi_array = []
    

    for i in range(len(base)):
        plaintext = d_shift(ciphertext, (i, base_type))
        key_array.append(i)
        plaintext_array.append(plaintext)
        chi_array.append(chi_squared(plaintext))
    
    # print(chi_array[0], plaintext_array[0], key_array[0])
    min_index = chi_array.index(min(chi_array))
    key = key_array[min_index]
    plaintext = plaintext_array[min_index]

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

    max_block_size = max(blocks, key=len)
    baskets = ['' for a in range(len(max_block_size))]
    i = 0

    for j in range(len(blocks)):
        while i < len(blocks):
            # baskets[j] = baskets[j] + blocks[i][j]
            if j < len(blocks[i]):
                baskets[j] = baskets[j] + blocks[i][j]
                # print(blocks[i][j])
            i+=1
        i = 0
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
    
    assert type(ciphertext) == str
    assert len(ciphertext)>0

    coin_index = index_of_coin(ciphertext)
    sum_freq = sum(get_freq(ciphertext))
    # print(coin_index)
    # print(sum_freq)
    # print(round(coin_index,4))

    knum = 0.0265*sum_freq
    kden = (0.065 - coin_index)+sum_freq*(coin_index-0.0385)

    k = knum/kden
    # print(k)

    k1 = math.floor(k)
    k2 = math.ceil(k) 
     
    if k2-k<=0.5:
        return [k2,k1]
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
    
    assert type(ciphertext) == str
    assert len(ciphertext) > 0

    match_array = []
    shifted_ciphertext = ciphertext
    nonalpha = utilities.get_base('nonalpha')

    # positions = utilities.get_positions(shifted_ciphertext, nonalpha + ' ' + '\n')
    ciphertext = utilities.clean_text(ciphertext, nonalpha + ' ' + '\n')
    shifted_ciphertext = utilities.clean_text(shifted_ciphertext, nonalpha + ' ' + '\n')
    # print(shifted_ciphertext)


    i = 1
    while i < CIPHER_SHIFT_FACTOR:
        # print(i)
        shifted_ciphertext = ' ' + shifted_ciphertext[:-1]
        # print(shifted_ciphertext)
        matches = compare_texts(ciphertext, shifted_ciphertext)
        match_array.append(matches)
        i+=1

    # print(match_array)
    max_matches = max(match_array)
    
    k1 = match_array.index(max_matches) + 1
    # print(k1)
    match_array[k1-1] = 0
    k1 = k1%max_key
    max_matches = max(match_array)
    # print(match_array)
    # print(match_array.index(max_matches))
    k2 = match_array.index(max_matches) + 1
    k2 = k2%max_key

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
    
    assert type(ciphertext) == str
    assert len(ciphertext) > 0

    fried = friedman(ciphertext)
    shift = cipher_shifting(ciphertext)

    # print(fried, shift)
    k1 = fried[0]
    k2 = fried[1]
    k3 = shift[0]
    k4 = shift[1]
    k_array = [k1,k2,k3,k4]

    if k1==k3 and k2!=k4 and k1!=k4:
        return [k1,k2,k4]
    elif k1!=k3 and k2==k4 and k1!=k4:
        return [k2,k1,k3]
    elif k1!=k3 and k2==k3 and k3!=k4:
        return [k2,k1,k4]
    elif k1==k4 and k1!=k2 and k3!=k4:
        return [k1,k2,k3]
    elif k1==k2 and k2==k3 and k3!=k4:
        return [k3,k4]
    elif k1!=k2 and k2==k3 and k3==k4:
        return [k1,k2]
    elif k1==k2 and k2!=k3 and k3==k4:
        return [k2,k3]
    elif k1==k2 and k2==k3 and k3==k4 and k1!=k3:
        return [k1,k3]
    elif k1==k2 and k2==k3 and k3==k4 and k2!=k4:
        return [k2,k4]
    
    return k_array

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
    
    assert type(ciphertext) == str
    assert len(ciphertext) > 0

    keys = _cryptanalysis_vigenere_key_length(ciphertext)
    for i in range(len(keys)):
        

    return key,plaintext

"""----------------------------
Columnar Transposition Cipher
----------------------------"""