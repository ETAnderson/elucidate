import requests
import json

sentence = 'what a big house'


def get_definition(word):
    word = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
    word_python_object = word.json()
    definition = dict(d.popitem() for d in word_python_object)

    print(json.dumps(definition, indent=4))

    return definition


def get_sentence_of_definitions(sentence):
    words = sentence.split()
    word_definitions = []

    for word in words:
        word_definition = get_definition(word)
        sentence_of_word_definitions = word_definitions.append(word_definition)

    return sentence_of_word_definitions

# print tests for get_definition function
# word_def = get_definition(word)
# print(word_def["meanings"])
# print(word_def["meanings"][1])
# print(word_def["meanings"][1]['partOfSpeech'])


# print tests for get_sentence_of_definitions function
sentence_definitions = get_sentence_of_definitions(sentence)
print(sentence_definitions)
