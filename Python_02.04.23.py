
try:

    string = input('Enter string:  ')
    symbol = input(' Enter the symbol you are looking for:  ')
    count = 0
    for i in string:
        if i == symbol:
            count +=1
    print(count)

except Exception as a:
    print(a)