
try:
    text = input('Enter text: ')[::-1]
    print(text)
except Exception as a:
    print(a)