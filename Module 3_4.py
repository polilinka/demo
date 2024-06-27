def single_root_words(root_word, *other_words):
    same_words = list()
    list_words = list(other_words)
    list1 = [s.lower() for s in list_words]
    root_word_lower = root_word.lower()
    for i in range(len(list1)):
        if (root_word_lower in list1[i]) or (list1[i] in root_word_lower):
            same_words.append(list_words[i])
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)