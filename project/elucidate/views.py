from django.shortcuts import render
from django.views import generic
from .models import Sentence, KnownWords, Word

import requests


class Elucidate(Sentence, KnownWords):
    def __init__(self):
        self.sentence = Sentence
        self.known_words = KnownWords
        self.word_definitions = []

    def get_definition(word):
        # pull definition fron dictionaryapi.dev and convert it from a json string into a dict
        word = str(word)
        word = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
        word_python_object = word.json()
        definition = dict(d.popitem() for d in word_python_object)

        return definition

    def remove_known_words(self):
        # check sentence words against list of known words
        sentence = self.sentence.split()
        sentence = [x for x in sentence if x not in self.known_words]

        return sentence

    def get_sentence_of_definitions(self, sentence):
        # compiles all the definitions into a sentence structure(list of json dict on a per word basis)
        word_definitions = []

        for word in sentence:
            definition = self.get_definition(word)
            word_definitions.append(definition)

        return word_definitions


class IndexView(generic.ListView):
    template_name = 'word.html'
    context_object_name = 'sentence_word_list'
