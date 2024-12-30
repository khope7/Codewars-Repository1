#"Hey fellow warriors"  --> "Hey wollef sroirraw" 
#"This is a test        --> "This is a test" 
#"This is another test" --> "This is rehtona test"

def spin_words(sentence):
    elements = sentence.split()
    bright = []
    for word in elements:
        if len(word) >= 5:
            for letter in word:
                bright.append(letter)
        else:
            print(word)

        print(bright)


sentence = "Hey fellow warriors"

spin_words(sentence)