def words(phrase):
    count_dict = {}
    phrase_list = phrase.split()

    for element in phrase_list:
        try:
            count_dict[int(element)] = phrase_list.count(element)
        except ValueError:
            count_dict[element] = phrase_list.count(element)
    return count_dict
