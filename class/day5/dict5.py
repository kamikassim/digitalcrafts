def word_histogram(paragraph):
    tally = {}
    wordList = paragraph.split()
    for word in wordList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1

    print tally

def top_three(tally):
    top_three_values = {}
    while len(top_three_values) <3
top_three(word_histogram('to be or not to be'))

#Lachlan will post the solution