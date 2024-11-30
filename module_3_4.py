def single_root_words (root_word, *other_words):
    same_words = []
    for i in (root_word, *other_words):
        if i == root_word:
            continue
        if (root_word.upper() in i.upper()) == True or (i.upper() in root_word.upper()) == True:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)