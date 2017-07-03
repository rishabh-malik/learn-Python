import random, string



letter_input_1=raw_input("What leter do you want? Enter v for vowel , c for constant , l for any letter: ")
letter_input_2=raw_input("What leter do you want? Enter v for vowel , c for constant , l for any letter: ")
letter_input_3=raw_input("What leter do you want? Enter v for vowel , c for constant , l for any letter: ")


def generator():
    vowels="aeiou"
    constants="bcdfghjklmnpqrstvwxyz"
    if letter_input_1=='v':
        letter1=random.choice(vowels)
    elif letter_input_1=='c':    
        letter1=random.choice(constants)
    elif letter_input_1=='l':    
        letter1=random.choice(string.ascii_lowercase)
    else: letter1=letter_input_1

    if letter_input_2=='v':
        letter2=random.choice(vowels)
    elif letter_input_2=='c':    
        letter2=random.choice(constants)
    elif letter_input_2=='l':    
        letter2=random.choice(string.ascii_lowercase)
    else: letter2=letter_input_2
    
    if letter_input_3=='v':
        letter3=random.choice(vowels)
    elif letter_input_3=='c':    
        letter3=random.choice(constants)
    elif letter_input_3=='l':    
        letter3=random.choice(string.ascii_lowercase)
    else: letter3=letter_input_3

    name=letter1+letter2+letter3
    return(name)

print generator()    