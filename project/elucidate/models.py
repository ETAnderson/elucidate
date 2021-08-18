from django.db import models


class Sentence(models.Model):
    sentence = models.CharField(max_length=140)

    def __str__(self):
        return self.sentence


class KnownWords(models.Model):
    known_word = models.CharField(max_length=40)

    def __str__(self):
        return self.known_word


class Word(models.Model):
    partOfSpeech = models.CharField(max_length=40)

    def __str__(self):
        return self.word


class PartOfSpeech(models.Model):
    word = models.ForeignKey(Word)
    partOfSpeech = models.CharField(max_length=40)

    def __str__(self):
        return self.partOfSpeech
