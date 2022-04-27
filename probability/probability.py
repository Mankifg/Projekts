import os

from black import out

def probability(fn, rpt, mode):
    output = 0
    if mode == 1:
        output = fn ** rpt
    elif mode == 2:
        for i in range(rpt):
            output += fn * (rpt - i)
    
    return output
os.system('cls')

print('Welcome to the Probability Calculator!')
num = int(input('Enter number of sequence >'))


print('And enter mode')
print('1. same - use same sequence')
print('2. low - sequence fall')
print('3. custom - custom sequence')
mode = int(input('Enter mode >'))

fn = int(input('Enter first number >'))

print(probability(fn, num, mode))




