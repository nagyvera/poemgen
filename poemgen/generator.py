#!/usr/bin/env python3

import pandas as pd #data structure
import numpy as np #data alignment
import glob # pathname matching
import random #randomization
from random import random 
import re #regex

# osszes kotet felhasznalasa
#in web:
file_names = glob.glob('poemgen/poemgen/kotetek/*.txt')

#in localhost:
#file_names = glob.glob('poemgen/kotetek/*.txt')

#in console:
#file_names = glob.glob('kotetek/*.txt')

# kotetek db szama ellenorzeskent: 
#print(len(file_names))

#beolvasas soronkent
def get_rows(file_name):
    with open(file_name, 'r') as f:
        return f.read().split('\n')
    
#mondatok beolvasasa
sentences = []
for file_name in file_names:
    sentences+=get_rows(file_name)

#tagolas tisztogatasa
sentences = [sentence.replace('\n','') for sentence in sentences]
sentences = [sentence.replace('\t','') for sentence in sentences]

# 1 dimenzios nd-tomb letrehozasa, ertekadas, eloszlas vizsgalat
lengths = [len(sentence) for sentence in sentences]
lengths = pd.Series(lengths)
lengths.quantile(.8)
lengths.describe()

#print(sentences)

#corpus keszites, tisztogatas
corpus = ""

for file_name in file_names:
    with open(file_name, 'r') as f:
            corpus+=f.read()
corpus = corpus.replace('\n',' ')
corpus = corpus.replace('\t',' ')
corpus = corpus.replace('“', ' " ')
corpus = corpus.replace('”', ' " ')
#oldalszamozas eltuntetese
corpus = corpus.replace('\-[0-9]+\-','')
corpus = corpus.replace('([0-9]+|[0-9]+\.|\d[0-9])','')
#zarojelek es egyeb egyedi karakterek eltuntetese
corpus = corpus.replace('(', '')
corpus = corpus.replace(')', '')
corpus = corpus.replace('*', '')
corpus = corpus.replace('*', '')
corpus = corpus.replace('-', '')
#tagolas megvalositasa mondatvegi jelek eseten
for spaced in ['.','-',',','!','?']:
    corpus = corpus.replace(spaced, ' {0} '.format(spaced))
    
#len(corpus)

#szokozonkent tordeles, szokozok eltavolitasa
corpus_words = corpus.split(' ')
corpus_words= [word for word in corpus_words if word != '']

#szoszures, egyedi szavak, indexeles
distinct_words = list(set(corpus_words))
word_idx_dict = {word: i for i, word in enumerate(distinct_words)}
distinct_words_count = len(list(set(corpus_words)))
#print(distinct_words)

#transition_mtx
next_word_matrix = np.zeros([distinct_words_count,distinct_words_count],dtype = bool)
#print(next_word_matrix)

for i, word in enumerate(corpus_words[:-1]):
    first_word_idx = word_idx_dict[word]
    next_word_idx = word_idx_dict[corpus_words[i+1]]
    next_word_matrix[first_word_idx][next_word_idx] +=1

def most_likely_word_after(aWord):
    most_likely = next_word_matrix[word_idx_dict[aWord]].argmax()
    return distinct_words[most_likely]

def weighted_choice(objects, weights):
    """ returns randomly an element from the sequence of 'objects', 
        the likelihood of the objects is weighted according 
        to the sequence of 'weights', i.e. percentages."""

    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    # standardization:
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]

from numpy.random import choice

def sample_next_word_after(aWord, alpha = 0):
    next_word_vector = next_word_matrix[word_idx_dict[aWord]] + alpha
    likelihoods = next_word_vector/next_word_vector.sum()
    return weighted_choice(distinct_words, likelihoods)

def stochastic_chain(seed, length=18):
    current_word = seed
    sentence = seed

    for _ in range(length):
        sentence+=' '
        next_word = sample_next_word_after(current_word)
        sentence+=next_word
        current_word = next_word
    return sentence

#ellenőrző hívás:
#print(stochastic_chain('Március'))