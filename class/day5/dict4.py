def word_histogram(paragraph):
    tally = {}
    wordList = paragraph.split()
    for word in wordList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1

    print tally

word_histogram('to be or not to be')