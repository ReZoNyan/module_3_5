def single_root_words(root_word, *other_words):
    same_words = []
    word = root_word.lower()
    for i in other_words:
        word_in_tuple = i.lower()
        if word in word_in_tuple:
            same_words.append(i)
        elif word_in_tuple in word:
            same_words.append(i)
    print(f'Список подходящих слов => {same_words}')


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bage')

#
root_word = str(input('Введите проверочное слово: '))
b = 1
my_list = []
while b == 1:
    c = str(input('Введите слово для добавление к проверяемому списку: '))
    if c == 'exit':
        b = 0
    else:
        my_list.append(c)

single_root_words(root_word, *my_list)
