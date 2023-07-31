def wordInTarget(word, target):
    '''
    Can a 'word', be made using letters from 'target'.
    '''
    targetlist = list(target)
    i = 0
    while i < len(word):
        letter = word[i]
        if letter in targetlist:
            targetlist.remove(letter)
            i += 1 
        else:
            return False
    return True
