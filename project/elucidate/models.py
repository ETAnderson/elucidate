from django.db import models


class Sentence(models.Model):
    sentence = models.CharField(max_length=140)


class KnownWords(models.Model):
    known_word = models.CharField(max_length=40)


class Word(models.Model):
    word = models.CharField(max_length=40)
    meaning = models.CharField(max_length=40)


class Meaning(models.Model):
    word = models.ForeignKey(Word)


class PartOfSpeech(models.Model):
    meaning = models.ForeignKey(Meaning)


class Definitions(models.Model):
    part_of_speech = models.ForeignKey(PartOfSpeech)
    definitions = models.CharField(max_length=600)


class Definition(models.Model):
    definition = models.ForeignKey(Definitions)
    example = models.CharField(max_length=280)
    synonyms = models.CharField(max_length=2000)
    antonyms = models.CharField(max_length=1000)


class Example(models.Model):
    definition = models.ForeignKey(Definition)


class Synonyms(models.Model):
    definition = models.ForeignKey(Definition)


class Antonyms(models.Model):
    definition = models.ForeignKey(Definition)
