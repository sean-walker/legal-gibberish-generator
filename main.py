'''
    main.py
    Sean Walker, Yale '19
    CPSC 185

    Runs the generator to create and generate from a model. Uses data parsed by the corpus parser to create model.
'''

from corpusParser import CorpusParser
from generator import Generator

def run_generator(num_words, word='If'):

    cp = CorpusParser()
    tokens = cp.get_tokens()
    gen = Generator(tokens)
    output = gen.generate(word, num=num_words)
    return output
