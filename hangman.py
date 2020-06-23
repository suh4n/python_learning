import random
from string import ascii_lowercase
print('H A N G M A N')
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice == 'play':
        words = 'python', 'java', 'kotlin', 'javascript'
        secret_word = random.choice(words)
        result = '-' * (len(secret_word))
        result_1 = list(result)
        mistakes = 0
        user_letters = []
        while True:
            if mistakes < 8:
                if '-' not in result_1:
                    print(f'You guessed the word {secret_word}!\nYou survived!')
                    break
                print()
                print(''.join(result_1))
                user_char = input('Input a letter: ')
                if len(user_char) != 1:
                    print('You should input a single letter')
                elif user_char not in ascii_lowercase:
                    print('It is not an ASCII lowercase letter')
                elif user_char in user_letters:
                    print('You already typed this letter')
                elif user_char in secret_word:
                    a = secret_word.find(user_char)
                    b = secret_word.rfind(user_char)
                    result_1[a] = user_char
                    result_1[b] = user_char
                    ''.join(result_1)
                elif user_char not in secret_word:
                    mistakes += 1
                    print('No such letter in the word')
                    ''.join(result_1)
                user_letters.append(user_char)
            else:
                print('You are hanged!')
                break
    elif user_choice == 'exit':
        break
    else:
        continue
