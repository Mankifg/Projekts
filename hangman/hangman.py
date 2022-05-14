import os
os.system('cls')
hangman = [
    "",
    "**```_____     \n    |/   |\n    |      \n    |      \n    |     \n    |      \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   ( )\n    |      \n    |     \n    |      \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |      \n    |     \n    |      \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |    |\n    |    \n    |   \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |   /|\n    |    \n    |   \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |   /|\\\n    |    \n    |   \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |   /|\\\n    |    |\n    |      \n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |   /|\\\n    |    |\n    |     |\n    |\n    |_______```**",
    "**```_____     \n    |/   |\n    |   (_)\n    |   /|\\\n    |    |\n    |   | |\n    |\n    |_______```**"
    ]
all_words  = []
hidden = []

mode = int(input('Enter mode:\n1. Set word\n2. Random word\n>'))
if mode == 1:
    word = input('vnesi besedo > ').lower()
if mode == 2:
    print('Using random words ()')
    
os.system('cls')
wrong = 0
attemp = 0

narobe = []
for i in range(len(word)):
    hidden.append('_')
  
  
while True:
    attemp = attemp + 1
    os.system('cls')
    print(hangman[wrong])
    print(f"You have {wrong} wrong guesses") 
    print(f'This is your {attemp} attempt.')
    message = ''
    for x in range(len(hidden)):
        message = message + " " + hidden[x]    
    print(message)

    player_input = input('Enter letter >').lower()
    
    if player_input == word:
        os.system('cls')
        print(f'You competed game Hangman with word "{word}" in {attemp} atemmpts')
        break
    
    inside = False
    for a in range(len(word)):
        if word[a] == player_input:
            hidden[a] = player_input
            inside = True
    if not inside:
        wrong = wrong + 1
        
    
    win = True
    for a in range(len(hidden)):
        if hidden[a] == "_":
            win = False
    if win:
        os.system('cls')
        print(f'You competed game Hangman with word "{word}" in {attemp} atemmpts')
        break
    
    if wrong == 9:
        print(f'You failed. > {word}')
        break            

