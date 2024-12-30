def order(sentence):
    if sentence == '':
        return ''
    else:
        sentence_list = sentence.split(" ")
        index = 1
        ordered_list = []

        while index <= len(sentence_list):
            for word in sentence_list:
                for letter in word:
                    if letter == str(index):
                        ordered_list.append(word)
                        index += 1
        
        final_sentence = " ".join(ordered_list)
        return final_sentence

    print(final_sentence)
            





order("is2 Thi1s T4est 3a") #  -->  "Thi1s is2 3a T4est"