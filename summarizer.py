from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

# stopwords are filler words
#https://www.mygreatlearning.com/blog/text-summarization-in-python/

def summarizer(text, length):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    wordFreqTable = {}
    for word in words:
        word = word.lower()
        #skip over stopwords
        if word in stopWords:
            continue
        if word in wordFreqTable:
            wordFreqTable[word] += 1
        else:
            wordFreqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceFreqTable= {}

    for sentence in sentences:
        for word, freq in wordFreqTable.items():
            if word in sentence.lower():
                if sentence in sentenceFreqTable:
                # each sentence will have the sum of the frequencies of words in it
                    sentenceFreqTable[sentence] += freq
                else:
                    sentenceFreqTable[sentence] = freq


    return nlargest(length, sentenceFreqTable, key=sentenceFreqTable.get)