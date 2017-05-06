'''
    corpusParser.py
    Sean Walker, Yale '19
    CPSC 185

    Parse Supreme Court conversation corpus into format for language modeling upon initialization.
'''

import nltk, sys, os.path, pickle
nltk.data.path.append('./nltk_data/')
from settings import APP_STATIC

class CorpusParser:

    def __init__(self):

        # constants
        delim = ' +++$+++ '
        corpus = 'sc.corpus'
        plain = 'sc.plain'
        tokenized = 'sc.tok'

        # parse corpus into plaintext
        if not os.path.exists(os.path.join(APP_STATIC, plain)):
            print ('Parsing corpus to plaintext...', end='')
            with open(os.path.join(APP_STATIC, corpus), 'r') as f1, open(os.path.join(APP_STATIC, plain), 'w') as f2:
                for line in f1:
                    parsed = line.split(delim)[7]
                    # remove pause indications
                    parsed = parsed.replace('--', '')
                    f2.write(parsed)
            print ('done')
        else:
            print ('Found plaintext file {}'.format(plain))

        if not os.path.exists(os.path.join(APP_STATIC, tokenized)):
            print ('Tokenizing plaintext...', end='')
            with open(os.path.join(APP_STATIC, plain), 'r') as f:
                tokens = []
                for line in f:
                    tokens += nltk.word_tokenize(line)
            self.tokens = tokens
            with open(os.path.join(APP_STATIC, tokenized), 'wb') as f:
                pickle.dump(self.tokens, f)
            print ('done')
        else:
            with open(os.path.join(APP_STATIC, tokenized), 'rb') as f:
                self.tokens = pickle.load(f)

    def get_tokens(self):
        return self.tokens
