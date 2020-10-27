import utilities
import A3_solution

def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Utilities Testing")
    print()
    
    print('-------------- Testing Compare Texts:')
    plaintext1 = utilities.file_to_text('plaintext1.txt')
    cut = [10,100,0,len(plaintext1)]
    for i in cut:
        plaintext2 = plaintext1[:i]+plaintext1[i+1:]
        print('Result{} = {}'.format(cut.index(i)+1,A3_solution.compare_texts(plaintext1,plaintext2)))
    print()
    
    print('-------------- Testing get_freq:')
    bases = [None,'lower','upper','nonalpha','special']
    for base in bases:
        print('Base = {}'.format(base))
        print(A3_solution.get_freq(plaintext1,base))
        print()
    
    print('-------------- Testing index_of_coin:')
    files = ['plaintext1.txt', 'plaintext2.txt','ciphertext1.txt', 'random_text.txt','lorem ipsum.txt','ciphertext2.txt','empty_file.txt']
    for file in files:
        text = utilities.file_to_text(file)
        print('I({},None) = \t{:.5f}'.format(file,A3_solution.index_of_coin(text)))
    print()
    bases = ['lower','alpha','alpha','upper','all']
    for i in range(5):
        text = utilities.file_to_text(files[i])
        print('I({},{}) = \t{:.5f}'.format(files[i],bases[i],A3_solution.index_of_coin(text,bases[i])))
    print()
    print('-------------- Testing chi_squared:')
    files = ['plaintext1.txt', 'plaintext2.txt','ciphertext1.txt', 'random_text.txt','lorem ipsum.txt','empty_file.txt']
    for file in files:
        text = utilities.file_to_text(file)
        print('chi_squared({}) = \t{:.3f}'.format(file,A3_solution.chi_squared(text)))
    print()
    
    print('End of Task 1: Utilities Testing')
    print('{}'.format('-'*40))
    print()
    return

def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: Vigenere Cipher Testing")
    print()
    
    print('-------------- Testing Vigenere Square:')
    print('Vigenere Square = ')
    square = A3_solution._vigenere_square()
    for row in square:
        print(row)
    print()
    
    print('-------------- Testing Vigenere Cipher (Autokey):')
    keys = ['R','i','A','']
    plaintext = utilities.file_to_text('plaintext1.txt')[:64]
    for key in keys:
        print('key = {}'.format(key))
        print('plaintext  = {}'.format(plaintext))
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        print('ciphertext = {}'.format(ciphertext))
        plaintext2 = A3_solution.d_vigenere(ciphertext,key)
        print('plaintext2 = {}'.format(plaintext2))
        if plaintext == plaintext2:
            print('Validated')
        else:
            print('Validation Failed')
        print()
    print()
    
    print('-------------- Testing Vigenere Cipher (Running Key):')
    keys = ['Russia','Somalia','AA','']
    plaintext = utilities.file_to_text('plaintext2.txt')[:41]
    for key in keys:
        print('key = {}'.format(key))
        print('plaintext  = {}'.format(plaintext))
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        print('ciphertext = {}'.format(ciphertext))
        plaintext2 = A3_solution.d_vigenere(ciphertext,key)
        print('plaintext2 = {}'.format(plaintext2))
        if plaintext == plaintext2:
            print('Validated')
        else:
            print('Validation Failed')
        print()
    print()

    print('End of Task 2: Vigenere Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Shift Cipher Testing")
    print()
    
    print('-------------- Testing Encryption/Decryption:')
    plaintext = utilities.file_to_text('plaintext1.txt')
    keys = [(3,utilities.get_base('lower')), (35,utilities.get_base('upper')),
            (-3, utilities.get_base('lower')) , (14, None), (31,utilities.get_base('alphanum')), 
            (11,'cr')]
    for key in keys:
        print('key = {}'.format(key))
        print('plaintext = {}'.format(plaintext[101:181]))
        ciphertext = A3_solution.e_shift(plaintext,key)
        print('ciphertext= {}'.format(ciphertext[101:181]))
        plaintext2 = A3_solution.d_shift(ciphertext,key)
        print('plaintext2= {}'.format(plaintext2[101:181]))
        if plaintext == plaintext2:
            print('Validated')
        else:
            print('Validation Failed')
        print()
    
    invalid_keys = [100, [3,utilities.get_base('lower')], ('3',utilities.get_base('upper')),
                    (4,''),(5,'A'),(13,20)]
    for key in invalid_keys:
        A3_solution.e_shift(plaintext,key)
        A3_solution.d_shift(plaintext,key)
    print()
    
    print('-------------- Testing Cryptanalysis:')
    keys = [3,17,23,8]
    for key in keys:
        ciphertext = A3_solution.e_shift(plaintext,(key,None))
        print('ciphertext = {}'.format(ciphertext[:100]))
        key2,plaintext2 = A3_solution.cryptanalysis_shift(ciphertext)
        print('Cryptanalysis results: key = {}'.format(key2))
        print('plaintext2 = {}'.format(plaintext2[:100]))
        print()
        
    print('End of Task 3: Shift Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task4():
    print('{}'.format('-'*40))
    print("Start of Task 4: Vigenere Cryptanalysis Testing")
    print()
     
    print('-------------- Testing Blocks to Baskets:')
    text = 'CP460 is my favorite course in Fall 2020'
    sizes = [3,4,5]
    for size in sizes:
        blocks = utilities.text_to_blocks(text,size)
        print('blocks = {}'.format(blocks))
        baskets = A3_solution._blocks_to_baskets(blocks)
        print('baskets= {}'.format(baskets))
        print()
          
    print('-------------- Testing Freidman:')
 
    ciphertext = utilities.file_to_text('ciphertext2.txt')
    print('ciphertext =')
    print(ciphertext)
    friedman = A3_solution.friedman(ciphertext)
    print('friedman = {}'.format(friedman))
    print()
    
    countries = utilities.file_to_text('countries.txt').split('\n') 
    counter = 0
    plaintext = utilities.file_to_text('plaintext4.txt')
    for key in countries:
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        friedman = A3_solution.friedman(ciphertext)
        print('key = {:15s} len = {:2d} friedman = {}'.format(key,len(key),friedman),end='\t')
        if len(key) in friedman:
            print('Good')
            counter += 1
        else:
            print('Bad')
    print('Found {} out of {} keys'.format(counter,len(countries)))  
    print()
      
    print('-------------- Testing Cipher Shifting:')
    ciphertext = utilities.file_to_text('ciphertext2.txt')
    print('ciphertext =')
    print(ciphertext)
    cipher_shifting = A3_solution.cipher_shifting(ciphertext)
    print('cipher shifting = {}'.format(cipher_shifting))
    print()
    
    counter = 0
    for key in countries:
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        cipher_shifting = A3_solution.cipher_shifting(ciphertext)
        print('key = {:15s} len = {:2d} c_shifting = {}'.format(key,len(key),cipher_shifting),end='\t')
        if len(key) in cipher_shifting:
            print('Good')
            counter+=1
        else:
            print('Bad')
    print('Found {} out of {} keys'.format(counter,len(countries)))  
    print()
     
    print('-------------- Testing Cryptanalysis of Key Length:')
    counter = 0
    for key in countries:
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        keys = A3_solution._cryptanalysis_vigenere_key_length(ciphertext)
        print('key = {:15s} len = {:2d} keys = {} '.format(key,len(key),keys),end='\t')
        if len(key) in keys:
            print('Good')
            counter+=1
        else:
            print('Bad')
    print('Found {} out of {} keys'.format(counter,len(countries)))  
    print()
    
    print('-------------- Testing Cryptanalysis:')
    count = 0
    for key in countries:
        ciphertext = A3_solution.e_vigenere(plaintext,key)
        k,plaintext2 = A3_solution.cryptanalysis_vigenere(ciphertext)
        print('key = {:10s}\tplaintext2 = {}'.format(k,plaintext2[:56]))
        if k != '':
            count+= 1
    print('Found {} out of {} keys'.format(count,len(countries)))  

    print()
    
    print('End of Task 4: Vigenere Cryptanalysis Testing')
    print('{}'.format('-'*40))
    print()
    return

task1()
#task2()
#task3()
#task4()
