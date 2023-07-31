def count_occurences(input_string):
    
    input_string = input_string.split(', ')
    
    counter = {}
    output = []
    for i in input_string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    
    counter = {k: v for k, v in sorted(counter.items(), key=lambda counter: counter[1])}
    maxValue = max(counter, key=counter.get)
    keyOfHighestValue = counter[maxValue]
    copyOfKey = int(keyOfHighestValue)
    valuesInDic = list(counter.values())
    valuesInDic.remove(copyOfKey)
    
    if keyOfHighestValue in valuesInDic:
        output.append([maxValue,keyOfHighestValue])
        del counter[maxValue]
        for i in counter:
            if counter[i] == keyOfHighestValue:
                output.append([i,counter[i]])
    else:
        output.append([maxValue,keyOfHighestValue])

    
    return output
