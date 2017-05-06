'''
    generator.py
    Sean Walker, Yale '19
    CPSC 185

    Creates a language model from a word list.
'''
import nltk, random, string
nltk.data.path.append('./nltk_data/')

class Generator:

    def __init__(self, tokens):
        print('Initializing language model....')
        # bigram model
        self.model = nltk.ngrams(tokens, 2)
        self.cfd = nltk.ConditionalFreqDist(self.model)
        print('done')

    def generate(self, word, num):
        output = ''
        for i in range(num):
            arr = []
            for j in self.cfd[word]:
                for k in range(self.cfd[word][j]):
                    arr.append(j)
            # don't add space to punctuation
            output += (('' if word in string.punctuation or word == "'" else ' ') + word)
            # go to random word
            try:
                word = arr[int((len(arr))*random.random())]
            except IndexError:
                output = 'Error: word not found in training data. Please try something else :('
                return output
        # add a trace of grammaticality
        if output[:1] not in string.punctuation:
            output += '.'
        # remove first space
        return output[1:]
