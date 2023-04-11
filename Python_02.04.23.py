

try:

    string = input("Enter a string: ")
    word = input("Enter a word: ")
    count = 0
    for i in range(len(string)):
        if string[i:i+len(word)] == word:
            count += 1
    print("Тumber of searched words",word,"in a row",count)


except Exception as a:
    print(a)