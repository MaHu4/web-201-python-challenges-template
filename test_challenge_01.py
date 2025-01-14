# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count = 0 #new variable starting from 0
    for each_character in word:
        if each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o' or each_character == 'u': # : closes the if-statement
            count = count + 1 
    print(count)
    #RETURN STATEMENT --> must be always the last line; ends the function
    return count # returns count outside of the function to get the result; otherwise, the function returns NONE
  

def test_challenge_01_happy_case(): 
     assert count_vowels('Kaleidoscope') == 6   
     # test needs to start with test_; afterwards new test-name can be given
     # each test-name must be unique
     # we can change the word Kaleidoscope by any other word

def test_challenge_02_happy_case(): 
     assert count_vowels('Kundalini') == 4   
     # other number of vowels -p-> passed

def test_upper_vowel_case():
    assert count_vowels('AEIOU') == 0
     # --> passed
 
def test_challenge_Y_case(): 
     assert count_vowels('Yak') == 1   
     # test that y is not counted as vowel --> passed

def test_emty_case(): 
     assert count_vowels('') == 0 
    # --> passed

def test_no_vowel_case():
    assert count_vowels('KTMND') == 0
    # --> passed

def test_numbers_as_string_case():
    assert count_vowels('2022') == 0
     # --> passed