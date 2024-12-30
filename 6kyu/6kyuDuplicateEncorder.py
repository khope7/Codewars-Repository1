def duplicate_encode(word):
    phrase = []
    final_list = []
    for char in word:
        phrase.append(char.lower())
    for char in phrase:
        if phrase.count(char) > 1:
            final_list.append(')')
        elif phrase.count(char) == 1:
            final_list.append('(')
    final_word = "".join(final_list)
    print(final_word)







duplicate_encode('recede')










'''
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
'''