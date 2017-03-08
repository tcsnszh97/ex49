direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')


def scan(lexicon):
    list = [];
    words = lexicon.split()
    for index in range(len(words)):
        if words[index] in direction:
            first_word = ('direction',words[index])
            list.append(first_word)
        elif words[index] in verb:
            first_word = ('verb',words[index])
            list.append(first_word)
        elif words[index] in stop:
            first_word = ('stop',words[index])
            list.append(first_word)
        elif words[index] in noun:
            first_word = ('noun',words[index])
            list.append(first_word)
        elif is_number(words[index]):
            first_word = ('number',words[index])
            list.append(first_word)
        else:
            first_word = ('error',words[index])
            list.append(first_word)
    return list

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

