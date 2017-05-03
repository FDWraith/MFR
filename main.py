with open("book.txt", "r") as book:
    wordList = book.read().strip().split()

def find_word( word ):
    def match( a ):
        return a == word
    return len(filter( match, wordList ))

def find_word_list( wordlist ):
    for word in wordlist:
        print "%s: %s"%( word, find_word(word) )
    pass

def most_frequent_word():
    wordlist = { word for word in wordList }
    top = (0, "")
    for word in wordlist:
        val = find_word(word)
        top = top if top[0] >= val else (val, word)
    return "%s: %s"%(top[0], top[1])

def mostFreqV2():
    end = { }
    for word in wordList:
        if word not in end:
            end[word] = 1
        else:
            end[word] += 1
    top = (0, "")
    for item in end.keys():
        top = top if top[0] >= end[item] else (end[item], item )
    return "%s: %s"%(top[1], top[0])

print find_word("the")
find_word_list( ["the", "a", "wow"])
print mostFreqV2()
