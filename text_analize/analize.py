import os

from cv2 import RNG_NORMAL

os.system('cls')
print('Welcome to the Text Analizer')
print('Chose mode:')
print('1. get text from file')
print('2. get text from console')
mode = int(input('>'))
os.system('cls')
if mode == 1:
    file = input('Enter text file name >')
    if ".txt" not in file:
        file = file + ".txt"
    
    with open(file, 'r') as f:
        text = f.read()
elif mode == 2:
    text = input('Enter text >')
else:
    print('Wrong mode')
    exit()

os.system('cls')

print(f'Symbols in text:{len(text)}.')

diff = []
repeat = []
for i in range(len(text)):
    if not text[i] in diff:
        diff.append(text[i])
        
print(diff)
for i,v in enumerate(diff):
    repeat.append(text.count(v))
    
    
sort_mode = int(input('Sort mode: \n1. by count\n2. by symbol\n>'))
if sort_mode == 1:
    comb = []
    for i in range(len(repeat)):
        comb.append(f"{repeat[i]}|{diff[i]}")
    comb.sort(reverse=False)
    for i in range(len(comb)):
    
    
    
    
    
    
    
print(diff)
print(repeat)