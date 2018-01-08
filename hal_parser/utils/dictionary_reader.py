import sys
import gensim


def parse_dictionary(inputWords, outputFile, gloveFile):

    gensimModel = gensim.models.KeyedVectors.load_word2vec_format(gloveFile, binary=False)

    with open(outputFile, 'w', encoding='utf-8') as output:
        for word in inputWords:
            most_similar_words = gensimModel.wv.most_similar(positive=[word], topn=50)
            output.write("{} -> {}\n".format(word, ", ".join(__filterResults__(most_similar_words))))


def __filterResults__(listOfSimilarWords):
    newList = []
    for t in listOfSimilarWords:
        newList.append(str(t[0]).encode('utf-8'))
    return newList
