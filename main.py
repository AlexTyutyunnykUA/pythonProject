def sum_pairs(ints, s):
    numbers=[]
    indexes =[]
    while len(numbers)<1:
         numbers = [[ints[i], ints[j]] for i in range(len(ints)) for j in range(len(ints)) if
                   ints[i] + ints[j] == s and i != j]
    while len(indexes)<1:
        indexes = [[i, j] for i in range(len(ints)) for j in range(len(ints)) if
               ints[i] + ints[j] == s and i != j]
    res = []

    for i in range(len(indexes)-1):
        if numbers[i][0] != numbers[i + 1][1]:
            if indexes[i][1] > indexes[i + 1][1]:
                res.append(indexes[i + 1])
        res.append(indexes[i])

    if len(numbers) == 0: return None
    return [ints[res[0][0]], ints[res[0][1]]]


print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
