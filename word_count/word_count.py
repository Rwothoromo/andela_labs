def words(phrase):
    count_dict = {}
    phrase_list = phrase.split(' ')

    if '' in phrase_list:
        phrase_list.remove('')

    for i in phrase_list:
        if '\n' in i:
            phrase_list.remove(i)
            phrase_list += i.split('\n')

        if '\t' in i:
            phrase_list.remove(i)
            phrase_list += i.split('\t')

    for element in phrase_list:
        try:
            count_dict[int(element)] = phrase_list.count(element)
        except ValueError:
            count_dict[element] = phrase_list.count(element)

    print(phrase_list, count_dict)
    return count_dict
