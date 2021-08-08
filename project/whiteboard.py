import requests
# import json
# replace with model
sentence = 'what a big house'
known_words = ['what', 'a']


def get_definition(word):
    word = str(word)
    word = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
    word_python_object = word.json()
    definition = dict(d.popitem() for d in word_python_object)

    return definition


def remove_known_words(sentence):
    sentence = sentence.split()
    sentence = [x for x in sentence if x not in known_words]

    return sentence


def get_sentence_of_definitions(sentence):
    word_definitions = []

    for word in sentence:
        definition = get_definition(word)
        word_definitions.append(definition)
        # newworddef = print(word)
        # newworddef = print(word_definitions)

    return word_definitions

# print tests for get_definition function
# word_def = get_definition(word)
# print(word_def["meanings"])
# print(word_def["meanings"][1])
# print(word_def["meanings"][1]['partOfSpeech'])


# print test for remove_known_words function
print('start :' + sentence)
new_sentence = remove_known_words(sentence)
print(new_sentence)
# print tests for get_sentence_of_definitions function
sentence_definitions = get_sentence_of_definitions(new_sentence)
print(sentence_definitions)
