
try:
    string = input('Enter string:  ')
    symbol = 0
    digits = 0
    for i in string:
        if i.isalpha():
            symbol +=1
        elif i.isdigit():
            digits +=1
        else:
            print('bl')
    print('Symbols in string: ', symbol)
    print('Numbers in string: ', digits)
except Exception as a:
    print(a)