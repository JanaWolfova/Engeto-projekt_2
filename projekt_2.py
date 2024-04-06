"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bulls & Cows

author: Jana Wolfová

email: janarega@seznam.cz

discord: jana_73904

"""
 
import random


def generate_secret_number():
    """
    Funkce vrací tajné číslo ze čtyř unikátních číslic
    funkce zamíchá číslice od 0 do 9  a vrátí první čtyři číslice
    pokud bude první číslice 0, zpustí se znova
    """
    while True:
        digits = (list(range(10)))
        random.shuffle(digits)
        secret_number = ''.join(str(digit) for digit in digits[:4])
        if secret_number[0] != "0":     
            return secret_number




def guessing_check(secret_number:str, guesswork:str):
    
    """
    prochází zvolené číslice, 
    pokud je číslice z hádání (guesswork) na správném místě --> bulls
    pokud správná číslice ale na jiném místě --> cows
    """
    
    
    bulls = 0
    cows = 0
  
    for i in range(len(guesswork)):
        if guesswork[i] == secret_number[i]:
            bulls += 1
        elif guesswork[i] in secret_number:
            cows += 1
    return bulls, cows


def welcome():
    print("Hi there!")
    print("-" * 47) 
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    print("Enter a number:")
    print("-" * 47)


def main():
    """
    hlavní funkce pro hru Bulls and Cows,
    pozdraví uživatele a vyzve ho k zadání čtyřmístného čísla
    """
    welcome()
    secret_number = generate_secret_number()
    attempts = 0  # Inicializace počítadla pokusů
    

    #hra probíhá dokud nejsou všechny čísla uhodnuty.
    while True:
        guess = input(">>>  ", )

        attempts += 1

        # Kontrola délky vstupu zda jsou vše čísla
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a four-digit number.")
            continue
        
        # Kontrola opakujících se číslic
        if len(set(guess)) != 4:
            print("Invalid input. Please enter a number with non-repeating digits.")
            continue

        bulls, cows = guessing_check(secret_number, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
        if bulls == 4:
            print(f"Correct, you've guessed the right number \nin {attempts} {'guess! That\'s amazing!!' if attempts == 1 
                                                                              else 'guesses, that\'s perfekt!.' if 2 <= attempts <= 11 
                                                                              else 'guesses, that\'s average.' if 7 <= attempts <= 14
                                                                              else 'guesses, not so good...' if 15 <= attempts <= 30 
                                                                              else 'guesses >> Hell!! finally the end.'}")
            break
        print("-" * 47)  


if __name__ == "__main__":
    main()