

try:

    string = input('Enter string:  ')
    search_word = input('Enter word what looking for:  ')
    word_for_change = input('Enter replacement word:  ')
    print(string.replace(search_word,word_for_change))



except Exception as a:
    print(a)